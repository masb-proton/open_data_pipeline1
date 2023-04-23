import pandas as pd
from src.Foundation.default_pipeline.Isave import Isave
from src.Foundation.default_pipeline.Iimporter import IImporter, ImportData, AssetClass
from src.Foundation.default_pipeline.Ipipeline import Ipipeline
from src.Foundation.default_pipeline.Imodel import Imodel
from src.Foundation.default_pipeline.Iproccess import Iproccess
from src.Foundation.default_pipeline.IproccessMethod import IDataProcessor
import yfinance
from datetime import datetime


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


class DefaultProcess(Iproccess):

    def __init__(self, ):
        pass

    def Iproccess(self, DF: pd.DataFrame) -> pd.DataFrame:
        pass


class CSVSave(Isave):
    def Isave(self, tDF: pd.DataFrame) -> None:
        return tDF.to_csv("")


yf_import = yf_Import("SPY")
pd_df = yf_import._import()
asset_class = yf_import.find_asset_class()
all_data = yf_import.return_data()
print(all_data)
