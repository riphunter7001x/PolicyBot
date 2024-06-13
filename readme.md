# PolicyBot: For Your Car Insurance Inquiries 🚗💬


PolicyBot is an AI assistant designed to help you with car insurance inquiries. It leverages generative AI and retrieval-augmented generation (RAG) to provide accurate and contextual responses based on a predefined document.

## About ℹ️

PolicyBot is built to assist users with their car insurance questions. It uses the following technologies:
- **Streamlit**: For building the interactive web interface.
- **Hugging Face**: For embeddings and language model tasks.
- **Pinecone**: For storing and retrieving vectorized document data.
- **CohereRerank**: For compressing and ranking the retrieved contexts to generate meaningful responses.
- **RAGAS (Retrieval-Augmented Generation with Assessments)**: For evaluating response quality.

Try the [deployed app](https://policybot-car.streamlit.app/) and interact with PolicyBot!

### Documentation 📄

PolicyBot is based on the guidelines and information provided in [this document](https://assets.churchill.com/motor-docs/policy-booklet-0923.pdf).

## Features 🌟

- **Interactive Chat Interface**: Chat with PolicyBot in a conversational manner.
- **Contextual Responses**: Get answers based on the document context.
- **Easy to Use**: Simple interface designed for ease of use.

## Evaluation 📊

PolicyBot uses Retrieval-Augmented Generation with Assessments (RAGAS) for generating responses, ensuring relevance and accuracy based on the provided document.

### What is RAGAS? 🤔

RAGAS evaluates RAG pipelines using:
- **Question**: The query for the RAG pipeline.
- **Answer**: The generated response.
- **Contexts**: Input data to answer the question.
- **Ground Truths**: The correct answer.

## Evaluation Metrics 📈

| Metric            | Score |
|-------------------|-------|
| Context Precision | 0.908 |
| Faithfulness      | 0.813 |
| Answer Relevancy  | 0.851 |
| Context Recall    | 0.939 |
| Harmfulness       | 0.000 |

![Evaluation Metrics](https://github.com/riphunter7001x/PolicyBot/blob/main/experiment/chart.png)

## Installation 🛠️

### Prerequisites 📋

- Conda (Anaconda or Miniconda)
- Python 3.10

### Steps 🚀

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

## Usage 🚀

Access the app at `http://localhost:8501` in your web browser. Ask car insurance-related questions and receive answers based on the predefined document.

## Contact 📧

For questions or issues, please open an issue on GitHub or email me at [adi.varpe117@gmail.com](mailto:adi.varpe117@gmail.com).

---

### Deployed Application 🌐

Check out the [PolicyBot App](https://policybot-car.streamlit.app/)!
