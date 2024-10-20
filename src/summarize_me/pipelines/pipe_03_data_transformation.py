from src.summarize_me.config.configuration import ConfigurationManager
from src.summarize_me.elements.e_03_data_transformation import DataTransformation
from src.summarize_me.logging import logger

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
           
    def main(self): 
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()