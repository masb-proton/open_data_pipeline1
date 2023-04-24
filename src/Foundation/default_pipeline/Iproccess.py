from abc import ABC, abstractmethod
import pandas as pd
from src.Foundation.utils import ImportData, AssetClass


class Iproccess(ABC):
    @abstractmethod
    def __init__(self, import_data: ImportData):
        self.import_data = import_data

    @abstractmethod
    def processor(self) -> ImportData:
        pass
