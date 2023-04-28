from abc import ABC, abstractmethod, abstractproperty, ABCMeta
import pandas as pd
from src.Foundation.utils import ImportData, AssetClass
from typing import Protocol


class Processor(ABC):
    @abstractmethod
    def process(self, import_data: ImportData) -> ImportData:
        pass


class ProcessPipeline:

    def __init__(self, import_data: ImportData):
        self.import_data = import_data
        self.processed_data = import_data

    def run_processes(self):
        """
        Runs all abc methods future version might require more robust class filtering
        """
        for i in dir(self.__class__):
            attr = getattr(self.__class__, i)
            print(attr)
            if type(attr) is ABCMeta:
                self.processed_data = attr().process(self.import_data)


