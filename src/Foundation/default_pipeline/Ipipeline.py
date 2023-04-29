from abc import ABC, abstractmethod
import pandas as pd
from src.Foundation.default_pipeline.Imodel import Imodel
from src.Foundation.default_pipeline.IproccessMethod import ProcessingMethod


class ModelPipeline:
    def __init__(self, data_model: Imodel, data_processing: ProcessingMethod):
        self.data_model = data_model
        self.data_processing = data_processing
        self.result = None

    def run_pipeline(self):
        self.data_processing.run_data_proccess()
        self.data_model =self.data_model(self.data_processing.process_data.pd_data)
        self.result = self.data_model.run_model()
        return self.result