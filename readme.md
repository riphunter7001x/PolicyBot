# PolicyBot: For Your Car Insurance Inquiries

![PolicyBot Logo](https://your-logo-url.com/logo.png)  <!-- Replace with your actual logo URL if available -->

PolicyBot is an AI assistant designed to assist you with car insurance inquiries. It leverages the power of generative AI and retrieval-augmented generation (RAG) to provide accurate and contextual responses based on a predefined document.

## About

PolicyBot is built to help users with their car insurance questions. It uses the following technologies:
- **Streamlit**: For building the interactive web interface.
- **Hugging Face**: For embeddings and language model tasks.
- **Pinecone**: For storing and retrieving vectorized document data.
- **CohereRerank**: For compressing and ranking the retrieved contexts to generate meaningful responses.

You can try the deployed app [here](https://policybot-car.streamlit.app/).

### Documentation

PolicyBot is based on the guidelines and information provided in [this document](https://assets.churchill.com/motor-docs/policy-booklet-0923.pdf).

## Features

- **Interactive Chat Interface**: Allows users to interact with PolicyBot in a conversational manner.
- **Contextual Responses**: Provides responses based on the context retrieved from the specified document.
- **Easy to Use**: Simple and intuitive interface designed for ease of use.

## Evaluation

PolicyBot uses Retrieval-Augmented Generation with Assessments (RAGAS) for generating responses. This approach ensures that the responses are both relevant and accurate based on the provided document.

### What is RAGAS?

RAGAS is a framework that helps you evaluate your Retrieval Augmented Generation (RAG) pipelines. RAG denotes a class of LLM applications that use external data to augment the LLM’s context. There are existing tools and frameworks that help you build these pipelines but evaluating it and quantifying your pipeline performance can be hard. This is where ragas (RAG Assessment) comes in.

#### Ragas references the following data:

- **Question**: These are the questions your RAG pipeline will be evaluated on.
- **Answer**: The answer generated from the RAG pipeline and presented to the user.
- **Contexts**: The contexts passed into the LLM to answer the question.
- **Ground Truths**: The ground truth answer to the questions.

## Evaluation Metrics

Here are the evaluation metrics for PolicyBot:

| Metric               | Score   |
|----------------------|---------|
| Context Precision    | 0.9083  |
| Faithfulness         | 0.8132  |
| Answer Relevancy     | 0.8513  |
| Context Recall       | 0.9389  |
| Harmfulness          | 0.0000  |

![result Metrics](https://your-image-url.com/result_metrics.png)  <!-- Replace with the direct URL of your result_metrics.png image -->

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Conda (Anaconda or Miniconda)
- Python 3.10

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/riphunter7001x/PolicyBot.git
    cd PolicyBot
    ```

2. **Create a Conda environment:**

    ```bash
    conda create --name policybot python=3.10
    ```

3. **Activate the Conda environment:**

    ```bash
    conda activate policybot
    ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Usage

Once the app is running, you can access it in your web browser at `http://localhost:8501`. Interact with PolicyBot by asking questions related to car insurance, and receive helpful responses based on the predefined document.

## Contact

For any questions or issues, please open an issue on GitHub or contact me at [adi.varpe117@gmail.com](mailto:adi.varpe117@gmail.com).

---

### Deployed Application

Check out the deployed application: [PolicyBot](https://policybot-car.streamlit.app/)
