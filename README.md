# SummarizeMe - A Text Summarization MLOps Project

**SummarizeMe** is a fully operational MLOps project that leverages modern NLP techniques to summarize texts efficiently. It uses the Samsum dataset and a pre-trained Pegasus CNN model for handling text summarization tasks. The project demonstrates the entire lifecycle from data ingestion, validation, transformation, training, evaluation, and pipeline automation.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Setup Instructions](#setup-instructions)
- [Model Information](#model-information)
- [Docker Integration](#docker-integration)
- [API Endpoints](#api-endpoints)
- [CI/CD Pipeline](#cicd-pipeline)
- [Model Performance](#model-performance)
- [Contribution](#contribution)
- [License](#license)

## Project Overview

SummarizeMe is built to handle the end-to-end process of training and evaluating a text summarization model. The project uses the Samsum dataset for training and testing and a pre-trained Pegasus model for summarization. The MLOps pipeline is modularized, making it easy to understand, modify, and extend.

## Project Structure

```bash
SummarizeMe/
├── data/                       # Zip Datasets (Train, Validation, Test)
├── src/
│   └── summarize_me/
│       ├── entity/             # Data classes for configurations
│       ├── config/             # Configuration handling
│       ├── elements/           # Core steps (Data Ingestion, Validation, Transformation, Training)
│       ├── pipelines/          # Complete pipelines for each stage of the process
├── Trials/                     # Jupyter notebooks for experimentation and trials
│   ├── SummarizeMe.ipynb       # Trial for model performance
│   ├── Trial_01_Data_Ingestion.ipynb
│   ├── Trial_02_Data_Validation.ipynb
│   └── Trial_03_Data_Transformation.ipynb
│   └── Trial_04_Model_Trainer.py
│   └── Trial_05_Model_Evaluation.py
├── config/
│   └── config.yaml             # YAML configuration files
├── app.py                      # FastAPI app for interaction
├── Dockerfile                  # Docker configuration file
├── main.py                     # Entry point for running the pipeline
├── params.yaml                 # Model parameter configuration
├── .github/
    └── workflows/
        └── main.yaml           # CI/CD pipeline configuration
└── README.md                   # Project documentation
```

## Dataset

We utilize the [Samsum dataset](https://huggingface.co/datasets/Samsung/samsum), which contains human-annotated dialogues and corresponding summaries. The dataset can be downloaded directly from Hugging Face or using the link 8 below:
* [Download SummarizeMe Dataset](https://github.com/Sanju-Shrestha/SummarizeMe/raw/refs/heads/main/data/summarizme-data.zip)


## Setup Instructions
### Prerequisites

Ensure the following dependencies are installed:
* Python 3.8+
* Docker (for containerization)
* FastAPI (for API)
* GitHub CLI (optional, for contributing)

### Steps
1. Clone the repository:
```bash
git clone https://github.com/Sanju-Shrestha/SummarizeMe.git
cd SummarizeMe
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Set up the environment and configuration files:
* Update config/config.yaml with appropriate paths and parameters.
* Set model hyperparameters in params.yaml.

### Pipeline Stages

SummarizeMe uses a modular pipeline for processing and training the model. The steps are outlined as follows:

* Data Ingestion: Downloads and loads data from Hugging Face or a pre-downloaded dataset.
    - Code: src/summarize_me/pipelines/pipe_01_Data_Ingestion.py

* Data Validation: Ensures the integrity of the data by checking for missing values and schema mismatches.
    - Code: src/summarize_me/pipelines/pipe_02_Data_Validation.py

* Data Transformation: Tokenizes the text using the Pegasus tokenizer and prepares it for the model.
    - Code: src/summarize_me/pipelines/pipe_03_Data_Transformation.py

* Model Training: Fine-tunes the Pegasus model on the Samsum dataset.
    - Code: src/summarize_me/pipelines/pipe_04_Model_Trainer.py

* Model Evaluation: Evaluates the trained model's performance using standard text summarization metrics.
    - Code: src/summarize_me/pipelines/pipe_05_Model_Evaluation.py

* Model Prediction: Predicts the summarized output.
    - Code: src/summarize_me/pipelines/pipe_prediction.py

## Model Information
**Pegasus Model**

Pegasus (google/pegasus-cnn_dailymail) is a pre-trained text summarization model developed by Google, based on the Transformer architecture. It is specifically fine-tuned on the CNN/DailyMail dataset, which is widely used for abstractive summarization tasks.

Key characteristics of the Pegasus model:
* Abstractive Summarization: Unlike extractive methods that simply copy key sentences, Pegasus generates concise and human-readable summaries by understanding the context and rephrasing the input text.
* Pre-training with Gap Sentences: Pegasus introduces a unique pre-training objective called "Gap Sentences Generation" (GSG). In this approach, whole sentences are masked (i.e., removed), and the model learns to predict the missing sentences, making it highly effective for summarization tasks.
* Fine-tuning on Specific Tasks: The cnn_dailymail version of Pegasus has been fine-tuned on the CNN/DailyMail dataset, which contains news articles and corresponding summaries, making it particularly suitable for summarizing long news stories or dialogues.

For this project, we use the Pegasus model as it delivers state-of-the-art results for text summarization tasks, especially with dialogue-based text from the Samsum dataset.

**Transformer Architecture**

The Transformer is a deep learning architecture that revolutionized natural language processing (NLP). It is the backbone of Pegasus and many other state-of-the-art models like BERT, GPT, and T5.
Key Features of the Transformer:
* Attention Mechanism: The Transformer uses a mechanism called self-attention to weigh the importance of different words in a sentence, regardless of their position. This allows the model to focus on key parts of the text when generating summaries.
* Encoder-Decoder Structure: The model consists of two main components:
    - Encoder: Reads and processes the input text.
    - Decoder: Generates the summarized text based on the encoding.
* Parallelization: Unlike previous sequential models like RNNs, the Transformer can process all words in a sentence simultaneously, leading to faster training and inference.

In the Pegasus model, the Transformer encoder processes the input dialogue or text, and the decoder generates a concise summary based on its understanding of the input.

By utilizing the Transformer architecture, the Pegasus model can generate high-quality summaries with rich context and coherent phrasing, making it highly suitable for abstractive summarization tasks like those in the SummarizeMe project.

## Docker

*Dockerfile*
```bash
FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
```

## API Endpoints

SummarizeMe provides the following API endpoints via FastAPI:
* POST /predict: Generate a summary for a given text input.
* POST /train: Train the model on the dataset.
The app will be available at http://localhost:8080.

## CI/CD Pipeline

.github/workflows/main.yaml

1. Continuous Integration (CI)
* Linting and Unit Testing: The CI step includes simple linting and unit testing to verify the code quality. You can extend this step to include actual Python linters (like pylint, flake8) and unit tests with pytest to ensure correctness before proceeding to deployment.

2. Build and Push to Amazon ECR (Continuous Delivery)
* AWS Credentials Configuration:
    - The pipeline uses the GitHub Action aws-actions/configure-aws-credentials@v1 to authenticate with your AWS account using the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION stored in your GitHub Secrets.
* Amazon Elastic Container Registry (ECR):
    - This step builds the Docker image from your repository, tags it, and pushes it to Amazon ECR, a fully-managed Docker container registry that stores, manages, and deploys container images.

3. Continuous Deployment (CD)
* Pull and Run the Docker Image:
    - The deployment phase runs on a self-hosted runner, where the pipeline pulls the Docker image from Amazon ECR and runs it on a Docker container, exposing it via port 8080.
* Pruning Old Images and Containers:
    - The final step cleans up any previous Docker containers or images to free up disk space and maintain a clean environment.

## Contributing

Contributions are welcome! Feel free to raise issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sanju-Shrestha/SummarizeMe/blob/a5f243794c63b52ced51f96216f3f9a91d096afe/LICENSE) file for details.
