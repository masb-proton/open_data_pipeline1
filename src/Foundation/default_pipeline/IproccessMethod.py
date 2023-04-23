from src.Foundation.default_pipeline.Isave import Isave
from src.Foundation.default_pipeline.Iproccess import Iproccess
from src.Foundation.default_pipeline.Iimporter import IImporter


class IDataProcessor:

    def __init__(self, data_importer: IImporter, data_processor: Iproccess, ticker_saver: Isave):
        self.data_importer = data_importer
        self.data_processor = data_processor
        self.ticker_saver = ticker_saver

    def run_data_proccess(self, ticker: str):
        return NotImplemented
