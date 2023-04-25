from src.Foundation.default_pipeline.Isave import Isave
from src.Foundation.default_pipeline.Iproccess import Iproccess
from src.Foundation.default_pipeline.Iimporter import IImporter
from abc import ABC, abstractmethod
from typing import Type, Any

# Any way to type-hint
# Fix later
class ProcessingMethod:

    def __init__(self, data_importer: Any, data_processor: Any, saver: Any, ticker: str):
        """
        dataimporter: Importer
        dateprocessor: Iprocess
        ticker_save: ISave
        """
        self.data_importer = data_importer
        self.data_processor = data_processor
        self.saver = saver
        self.ticker = ticker

    def run_data_proccess(self):
        data_importer = self.data_importer(self.ticker)
        import_data = data_importer.return_data()

        data_processor = self.data_processor(import_data)
        processed_data = data_processor.processor()
        saver = self.saver(processed_data)
        saver_data = saver.save()

        return saver_data
