from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch the Pinecone and Cohere API keys from the environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Set the API keys in the environment variables for the session
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

# Function to download Hugging Face embeddings model
def download_hugging_face_embeddings():
    """
    Download the Hugging Face embeddings model.

    Returns:
        HuggingFaceEmbeddings: Initialized Hugging Face embeddings object.
    """
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

# Download Hugging Face embeddings model
embeddings = download_hugging_face_embeddings()

# Define the name of the Pinecone index
index_name = "policybot"

# Initialize Pinecone vector store with the downloaded embeddings
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

# Initialize the CohereRerank compressor
compressor = CohereRerank()

# Create a reranking retriever using ContextualCompressionRetriever
# - base_compressor: CohereRerank compressor
# - base_retriever: Pinecone vector store as a retriever with search parameters
rerank_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever(search_kwargs={"k": 7})
)
