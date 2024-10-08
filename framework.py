# Importing the libraries

from datetime import datetime
from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

print(datetime.now())

package_name = 'summarize_me'

files_list = [
    Path('.github') / 'workflows' / '.gitkeep',
    f'src/__init__.py'
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/elements/__init__.py',
    f'src/{package_name}/elements/e_01_data_ingestion.py',
    f'src/{package_name}/elements/e_02_data_validation.py',
    f'src/{package_name}/elements/e_03_data_transformation.py',
    f'src/{package_name}/elements/e_04_model_trainer.py',
    f'src/{package_name}/elements/e_05_model_evaluation.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/utils/commons.py',
    f'src/{package_name}/logging/__init__.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/config/configuration.py',
    f'src/{package_name}/pipelines/__init__.py',
    f'src/{package_name}/pipelines/pipe_01_data_ingestion.py',
    f'src/{package_name}/pipelines/pipe_02_data_validation.py',
    f'src/{package_name}/pipelines/pipe_03_data_transformation.py',
    f'src/{package_name}/pipelines/pipe_04_model_trainer.py',
    f'src/{package_name}/pipelines/pipe_05_model_evaluation.py',
    f'src/{package_name}/pipelines/pipe_prediction.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/entity/config_entity.py',
    f'src/{package_name}/constants/__init__.py',
    f'src/{package_name}/exception.py',
    f'src/{package_name}/logger.py',
    'config/config.yaml',
    'metrics_threshold.yaml',
    'params.yaml',
    'main.py',
    'app.py',
    'setup.py',
    'Dockerfile',
    'requirements.txt',
    'requirements_dev.txt',
    'trials/trial_01_data_ingestion.ipynb',
    'trials/trial_02_data_validation.ipynb',
    'trials/trial_03_data_transformation.ipynb',
    'trials/trial_04_model_trainer.ipynb',
    'trials/trial_05_model_evaluation.ipynb',
    'trials/trial_06_model_validation.ipynb',
    'trials/SummarizeMe.ipynb',
    'trials/trials.ipynb'

]

# Traversing through each file from the list
for filepath in files_list:
    filepath = Path(filepath)

    # Splitting the filename and directory from the filepath
    filedir, filename = os.path.split(filepath)

    # Creating new folders if not present
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory:{filedir} for the file {filename}')

    # Creating empty file if not present or empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file : {filepath}')

    else:
        logging.infor(f'{filename} already exists')

