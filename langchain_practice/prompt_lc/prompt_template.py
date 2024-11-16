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

# # Display the Prompt
# print(f"\nHere is the first Method Prompt  : \n{promptData1}\n")
# print(f"Here is the Second Method Prompt : \n{promptData2}\n")


# Example No 2 --> Prompt Having One Input Variable

# Method No 1
promptSInput1 = PromptTemplate(
    input_variables = ["language_name"] , template = "Tell me about {language_name} language."
).format(language_name = "python")

# Method No 2:
promptSInput2 = PromptTemplate.from_template("tell me about {language_name} language.").format(language_name = "java")

# Display the Prompt
print(f"\nHere is the First Method Prompt : \n{promptSInput1}\n")
print(f"Here is the Second Method Prompt : \n{promptSInput2}\n")