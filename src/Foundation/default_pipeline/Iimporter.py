from abc import ABC, abstractmethod
import pandas as pd
from dataclasses import dataclass
from typing import Union


class AssetClass:
    class ETF:
        pass

    class CryptoCurrency:
        pass

    class Stock:
        pass

    class MLP:
        pass

    class Forex:
        pass


@dataclass
class ImportData:
    pd_data: pd.DataFrame
    asset_class: Union[AssetClass.ETF, AssetClass.Stock, AssetClass.CryptoCurrency, AssetClass.MLP, AssetClass.Forex]


class IImporter(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _import(self):
        pass

    @abstractmethod
    def find_asset_class(self) -> ImportData:
        pass
