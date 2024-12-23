# Import the Important Modules
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter , CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


# Define the Prompt for this Project
promptTemplate = PromptTemplate(
    input_variables=["context"],  # Include the "context" input variable
    template="You are a helpful assistant. Provide the Summarization of the following Document:\n{context}"
)
# Read the Document File
DOC_PATH = "../../PDF_Files/machine_learning_overview.pdf"
loader = PyPDFLoader(DOC_PATH)
pages  = loader.load()

# Convert Pages into the Chunks using the Text Splitter Method
splitter = RecursiveCharacterTextSplitter(separators = "\n" , chunk_size = 200 , chunk_overlap = 50)
doc      = splitter.split_documents(pages)

# Apply the HuggingFace OpenSource Embedding
MODEL_NAME = "all-MiniLM-L6-v2"
embedding = HuggingFaceEmbeddings(model_name = MODEL_NAME)
#embedded_text = embedding.embed_documents([chunk.page_content for chunk in doc])

# Create the OLLAMA Opensource Model for LLM
OLLAMA_MODEL_NAME = "llama3.2"
llm = OllamaLLM(model = OLLAMA_MODEL_NAME)

# store the Embedding & Chinks Data in the Vector Store
vector = FAISS.from_documents(doc , embedding)
retriever = vector.as_retriever(search_type="similarity")


# Define the Chain for further Process
combine_docs_chain = create_stuff_documents_chain(llm=llm, prompt=promptTemplate)

chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=combine_docs_chain  # Use the combine_docs_chain here
)
summary = chain.invoke({"input": "Summarize the document"})
print(summary)