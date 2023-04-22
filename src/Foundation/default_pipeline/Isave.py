from abc import ABC, abstractmethod
import pandas as pd

class Isave(ABC):
    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def Isave(self, tDF: pd.DataFrame) -> None:
        pass
