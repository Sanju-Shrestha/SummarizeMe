from src.summarize_me.pipelines.pipe_01_data_ingestion import DataIngestionPipeline
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