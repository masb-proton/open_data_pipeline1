from abc import ABC, abstractmethod
import pandas as pd
from SRC.Foundation.deafault_Pipeline.Imodel import Imodel
from SRC.Foundation.deafault_Pipeline.IproccessMethod import IDataProcessor


class Ipipeline:
    def __init__(self, data_model: Imodel, data_processing: IDataProcessor):
        self.data_model = data_model
        self.data_processing = data_processing

    def run_pipeline(self):
        pass
