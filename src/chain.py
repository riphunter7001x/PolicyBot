from langchain.schema.runnable import RunnableSequence,RunnableParallel, RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from src.helper import rerank_retriever
from src.prompt import PROMPT
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch the GROQ API key from the environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set the GROQ API key in the environment variables for the session
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize the ChatGroq large language model with the specified model name
llm = ChatGroq(
    model="llama3-70b-8192"
)

# Create a chain for question-answer generation
# The chain involves:
# 1. Retrieving the context using the rerank_retriever function.
# 2. Passing the question through without modification.
# 3. Applying a prompt template to format the input for the LLM.
# 4. Using the LLM (ChatGroq) to generate a response.
# 5. Parsing the LLM output into a string format.
# Define your steps

LLMchain = (
    {
        "context": rerank_retriever,
        "question":  RunnablePassthrough(),
    }
    | PROMPT
    | llm
    | StrOutputParser()
)