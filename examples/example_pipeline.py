import pandas as pd
from src.Foundation.default_pipeline.Isave import Isave
from src.Foundation.default_pipeline.Iimporter import IImporter
from src.Foundation.default_pipeline.Ipipeline import ModelPipeline
from src.Foundation.utils import ImportData, AssetClass
from src.Foundation.default_pipeline.Imodel import Imodel
from src.Foundation.default_pipeline.Iproccess import Processor, ProcessPipeline
from src.Foundation.default_pipeline.IproccessMethod import ProcessingMethod
import yfinance


# Creating import method
class yf_Import(IImporter):
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.data_ticker = yfinance.Ticker(self.ticker)
        self.data = self.data_ticker.history("max")

    def _import(self) -> pd.DataFrame:
        return self.data

    def find_asset_class(self) -> str:
        return self.data_ticker.info['quoteType']

    # {"data": self._import(), "quoteType": self._import()}
    def return_data(self) -> ImportData:
        data_dict = {"EQUITY": AssetClass.Stock, "ETF": AssetClass.ETF}
        yf_asset_type = self.find_asset_class()
        return ImportData(self._import(), data_dict[yf_asset_type])


# Define the process pipeline
class ImplementedPipeline(ProcessPipeline):
    ##################################################### User defined classes
    # Add processor to list
    class AddProcessor(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            print(self.__class__)
            import_data.pd_data = import_data.pd_data + 1
            print(import_data.pd_data)
            return import_data

    # Add processor to list
    class RemoveRowProcessor(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            print(self.__class__)
            import_data.pd_data = import_data.pd_data.drop("High", axis=1)
            print(import_data.pd_data)
            return import_data

    class MakeRandomOperation(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            print(self.__class__)
            import_data.pd_data = import_data.pd_data + 2
            print(import_data.pd_data)
            return import_data


# Define Save class
class CSVSave(Isave):
    def save(self) -> ImportData:
        return self.import_data


class LinearModel(Imodel):

    def __init__(self):
        pass

    def run_model(self, DF: pd.DataFrame) -> pd.DataFrame:
        pass


pm = ProcessingMethod(yf_Import, ImplementedPipeline, CSVSave, "SPY")
# ModelPipeline(LinearModel, pm)
print(pm.run_data_proccess())
