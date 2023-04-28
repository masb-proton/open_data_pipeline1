from abc import ABC, abstractmethod
import pandas as pd
from src.Foundation.default_pipeline.Imodel import Imodel
from src.Foundation.default_pipeline.IproccessMethod import ProcessPipeline


class ModelPipeline:
    def __init__(self, data_model: Imodel, data_processing: ProcessPipeline):
        self.data_model = data_model
        self.data_processing = data_processing

    def run_pipeline(self):
        pass
