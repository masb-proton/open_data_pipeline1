from src.Foundation.default_pipeline.Isave import Isave
from src.Foundation.default_pipeline.Iproccess import Processor, ProcessPipeline
from src.Foundation.default_pipeline.Iimporter import IImporter
from abc import ABC, abstractmethod
from typing import Type, Any


# Any way to type-hint
# Fix later
class ProcessingMethod:

    def __init__(self, data_importer: IImporter, process_pipeline: ProcessPipeline, saver: Isave, ticker: str):
        """
        dataimporter: Importer
        dateprocessor: Iprocess
        ticker_save: ISave
        """
        self.data_importer = data_importer
        self.process_pipeline = process_pipeline
        self.saver = saver
        self.ticker = ticker

    def run_data_proccess(self):
        data_importer = self.data_importer(self.ticker)
        import_data = data_importer.return_data()

        pipeline_processor = self.process_pipeline(import_data)
        processed_data = pipeline_processor.run_processes()
        print(processed_data)
        saver = self.saver(processed_data)
        saver_data = saver.save()

        return saver_data

# protocol
