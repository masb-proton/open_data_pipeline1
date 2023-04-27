from abc import ABC, abstractmethod
import pandas as pd
from src.Foundation.utils import ImportData, AssetClass
from typing import Protocol


class Iproccess(Protocol):

    def __init__(self, import_data: ImportData):
        self.import_data = import_data

    @abstractmethod
    def processor(self) -> ImportData:
        pass


class IprocessPipe(ABC):
    @abstractmethod
    def __init__(self, Iproccess_list: [Iproccess], import_data: ImportData):
        pass

    @abstractmethod
    def run_process_pipe(self):
        pass


