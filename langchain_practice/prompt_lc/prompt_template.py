# Import the All Important Modules
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter , RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate

# Example No 1: --> Prompt Without Inputs Variables

# method No 1
promptData1 = PromptTemplate(
        input_variables = [] , template = "Tell me about Python Language"
).format()

# Method No 2
promptData2 = PromptTemplate.from_template("Tell me about Python Language").format()

# Display the Prompt
print(f"\nHere is the first Method Prompt  : \n{promptData1}\n")
print(f"Here is the Second Method Prompt : \n{promptData2}\n")
