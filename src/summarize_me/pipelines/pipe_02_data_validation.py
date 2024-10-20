from src.summarize_me.config.configuration import ConfigurationManager
from src.summarize_me.elements.e_02_data_validation import DataValidation
from src.summarize_me.logging import logger

class DataValidationPipeline:
    def __init__(self) -> None:
        pass
           
    def main(self): 
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
