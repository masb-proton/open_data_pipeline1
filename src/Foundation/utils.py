from typing import Union
import pandas as pd
#test
from dataclasses import dataclass


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
