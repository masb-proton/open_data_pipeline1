from abc import ABC, abstractmethod
import pandas as pd
from src.Foundation.utils import ImportData

class Isave(ABC):

    def __init__(self, import_data: pd.DataFrame):
        self.import_data = import_data

    @abstractmethod
    def save(self):
        pass
