from abc import ABC, abstractmethod
import pandas as pd
from src.Foundation.utils import ImportData

class Isave(ABC):

    def __init__(self, import_data: ImportData):
        self.import_data = import_data

    @abstractmethod
    def save(self) -> ImportData:
        pass
