from abc import ABC, abstractmethod
import pandas as pd
from src.Foundation.default_pipeline.Imodel import Imodel
from src.Foundation.default_pipeline.IproccessMethod import Iproccess


class Ipipeline:
    def __init__(self, data_model: Imodel, data_processing: Iproccess):
        self.data_model = data_model
        self.data_processing = data_processing

    def run_pipeline(self):
        pass
