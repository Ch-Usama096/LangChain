# Import the Modules 
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter , RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

# Define the Prompt 
promptTemplate = PromptTemplate(
    input_variables = ["language_name"] , template = "Tell me about this {language_name} language."
)

# Define the LLM Model for the Question 
MODEL_NAME = "llama3.2"
llm = OllamaLLM(model = MODEL_NAME)

# Define the Chain for run the multiple sequences
chain = LLMChain(llm = llm , prompt = promptTemplate)

# Run the LLM Model for the Answer the Question
res = chain.invoke({"language_name" : "python"})

# Display the Answers
print(res)