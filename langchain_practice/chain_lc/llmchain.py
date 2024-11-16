# Import the All Important Modules
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter , RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate # For LLM Model
from langchain_core.prompts import ChatPromptTemplate , SystemMessagePromptTemplate , HumanMessagePromptTemplate # For the Chat Model

from langchain_ollama import OllamaLLM


# Load the Ollama Model 
llm = OllamaLLM(model = "llama3.2")


# Define the Prompt Template
prompt = PromptTemplate(
    input_varaibles = ["person_name"]  , template = "tell me about this {person_name} person"
).format(person_name ="Muhammad Ali")


