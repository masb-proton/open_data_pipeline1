import pandas as pd

from src.Foundation.default_pipeline.Isave import Isave
from src.Foundation.default_pipeline.Iimporter import IImporter
from src.Foundation.default_pipeline.Ipipeline import Ipipeline
from src.Foundation.default_pipeline.Imodel import Imodel
from src.Foundation.default_pipeline.Iproccess import Iproccess
from src.Foundation.default_pipeline.IproccessMethod import IDataProcessor
import yfinance
from datetime import datetime


# Creating Simple import method
class yf_Import(IImporter):
    def __init__(self):
        pass

    def _import(self, ticker: str) -> pd.DataFrame:
        data = yfinance.Ticker(ticker)
        data.history("max")
        todayDate = datetime.now()
        data = data.history(start="2014-09-17", end=todayDate)
        return data

    def find_asset_class(self):
        return NotImplemented

class CSVSave(Isave):
    def Isave(self, tDF: pd.DataFrame) -> None:
        pass

yf_import = yf_Import()._import("F")
print(yf_import)
csv_import = CSVSave().
