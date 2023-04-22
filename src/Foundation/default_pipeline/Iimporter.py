from abc import ABC, abstractmethod
import pandas as pd


class IImporter(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _import(self, ticker: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def find_asset_class(self):
        pass


