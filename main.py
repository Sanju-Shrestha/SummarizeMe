from src.summarize_me.pipelines.pipe_01_data_ingestion import DataIngestionPipeline
from src.summarize_me.pipelines.pipe_02_data_validation import DataValidationPipeline
from src.summarize_me.pipelines.pipe_03_data_transformation import DataTransformationPipeline
from src.summarize_me.pipelines.pipe_04_model_trainer import ModelTrainerPipeline
from src.summarize_me.logging import logger

ELEMENT_01_NAME = "DATA INGESTION ELEMENT"
try:
    logger.info(f"## =================== {ELEMENT_01_NAME} Started! ========================##")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"## =============== {ELEMENT_01_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logger.exception(e)
    raise e

ELEMENT_02_NAME = "DATA VALIDATION ELEMENT"
try:
    logger.info(f"## =================== {ELEMENT_02_NAME} Started! ========================##")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f"## =============== {ELEMENT_02_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logger.exception(e)
    raise e

ELEMENT_03_NAME = "DATA TRANSFORMATION ELEMENT"
try:
    logger.info(f"## =================== {ELEMENT_03_NAME} Started! ========================##")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f"## =============== {ELEMENT_03_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logger.exception(e)
    raise e

ELEMENT_04_NAME = "MODEL TRAINER ELEMENT"
try:
    logger.info(f"## =================== {ELEMENT_04_NAME} Started! ========================##")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    logger.info(f"## =============== {ELEMENT_04_NAME} Terminated Successfully!=================\n\nx************************x")
except Exception as e:
    logger.exception(e)
    raise e