from abc import ABC, abstractmethod
import pandas as pd
class Iproccess(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def Iproccess(self, DF: pd.DataFrame) -> pd.DataFrame:
        pass
