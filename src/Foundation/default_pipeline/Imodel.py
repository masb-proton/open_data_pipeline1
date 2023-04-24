from abc import ABC, abstractmethod
import pandas as pd


class Imodel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def run_model(self, DF: pd.DataFrame) -> pd.DataFrame:
        pass
