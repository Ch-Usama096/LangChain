# Import the Important Modules
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter , RecursiveCharacterTextSplitter


# Part 1

# Read the PDF File
FILE_PATH = "../../PDF_Files/machine_learning_overview.pdf"
loader = PyPDFLoader(FILE_PATH)
pages  = loader.load()

# Display the Length & Types of the Pages
print(f"\nHere is the Length of the Pages : {len(pages)}")
print(f"Here is the Type of the   Pages : {type(pages)}")

# Display the MetaData & Page Content Data
print(f"Here is the Meta Data of First Page : {pages[0].metadata}")
print(f"Here is the Page Content of the First Page : {pages[0].page_content[:102]}")


# Part 2

# Define the RecursiveCharacterTextSplitter
textSplitter = RecursiveCharacterTextSplitter(chunk_size = 100 , chunk_overlap = 15 , separators = "\n")

# Split the Document into Chunks
doc = textSplitter.split_documents(pages)

# Display the Lenght of the Doc after converting the Chunks
print(f"\nHere is the Length of the Docment After Chunks : {len(doc)}")

# Display the Data from the DOC
print(f"Display the Page Content Data from the 10 Page : {doc[10].page_content[:100]}\n")

# Display the Length of the Each Page from the Doc
print("Display the Length of Each Page : ")
[print(len(doc[index].page_content)) for index in range(0,len(doc))]