from SRC.Foundation.deafault_Pipeline.Isave import Isave
from SRC.Foundation.deafault_Pipeline.Iproccess import Iproccess
from SRC.Foundation.deafault_Pipeline.Iimporter import Iimporter



class IDataProcessor:

    def __init__(self,data_importer: Iimporter, data_processor: Iproccess, ticker_saver: Isave):
        self.data_importer = data_importer
        self.data_processor = data_processor
        self.ticker_saver = ticker_saver

    def run_data_proccess(self, ticker: str):
        return NotImplemented




