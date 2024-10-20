from src.summarize_me.config.configuration import ConfigurationManager
from src.summarize_me.elements.e_04_model_trainer import ModelTrainer
from src.summarize_me.logging import logger

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass
           
    def main(self): 
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()