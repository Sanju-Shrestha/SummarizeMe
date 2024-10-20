from src.summarize_me.config.configuration import ConfigurationManager
from src.summarize_me.elements.e_01_data_ingestion import DataIngestion
from src.summarize_me.logging import logger

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
           
    def main(self): 
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    