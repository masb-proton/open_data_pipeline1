from abc import ABC, abstractmethod
import pandas as pd
from dataclasses import dataclass
from typing import Union
from src.Foundation import utils
from typing import Protocol


class IImporter(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _import(self):
        pass

    @abstractmethod
    def find_asset_class(self) -> str:
        pass

    @abstractmethod
    def return_data(self) -> utils.ImportData:
        pass