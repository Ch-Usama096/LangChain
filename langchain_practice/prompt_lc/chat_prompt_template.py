# Import the Important Modules

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter , CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate # For the LLM Prompt
from langchain_core.prompts import ChatPromptTemplate , HumanMessagePromptTemplate , SystemMessagePromptTemplate # For the Chat Model Prompt


#                           Prompt For Chat Models

# Method No 1   --> Simple Method Using
chatModelPrompt1 = ChatPromptTemplate.from_messages([
    ("system" , "You are a helpful assistant that translate {input_lang} to {output_lang}."),
    ("human" , "{text}")
]).format_messages(
    input_lang  = "English",
    output_lang = "Spanish",
    text = "My Name is Usama Husnain"
)
# Display the Chat Model Prompt
# print(f"\nHere is the Prompt for Chat Model : \n{chatModelPrompt1}\n")

# Method No 2 --> Using Message Class
system_template  = "You are a helpfull assistant that translate {input} to {output}"
human_template   = "{text}"
ChatModelPrompt2 = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template)
]).format(input = "English" , output = "Spanish" , text = "My Name is Usama Husnian")

# Display the Chat Model Prompt
print(f"\nHere is the Prompt for Chat Model : \n{ChatModelPrompt2}\n")


