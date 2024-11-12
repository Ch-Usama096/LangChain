# Import the All Important Modules
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter , CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings


from sklearn.metrics.pairwise import cosine_similarity

# Read the PDF File
FILE_PATH = "../../PDF_Files/machine_learning_overview.pdf"
loader = PyPDFLoader(FILE_PATH)
pages = loader.load()

# Display the Length of the Pages
# print(f"\nHere is the Length of the Pages : {len(pages)}")
# print(f"Here is the Meta Data of the Page : {pages[0].metadata}")
# print(f"Here is the Content of the Page   : \n{pages[0].page_content[:103]}")

# Convert the Pages Data int Chunks 
splitter = RecursiveCharacterTextSplitter(chunk_size = 100 , chunk_overlap = 20 , separators = "\n")

doc = splitter.split_documents(pages)

# Display the Length of the Doc after changed Chunks
# print(f"\nHere is the Length of the Doc : {len(doc)}")


# Convert the Vector (Using OpenSource Models)


# Part No 1 (HuggingFace Langchain  OpenSource Embeddings) --> https://python.langchain.com/docs/integrations/providers/huggingface/

MODEL_NAME_EMB = "all-MiniLM-L6-v2"
# embedding      = HuggingFaceEmbeddings(model_name = MODEL_NAME_EMB)

# # Convert the Doc into Embedding
# text_embed = embedding.embed_documents([chunk.page_content for chunk in doc])
# # Display the Chunk No & Embedding Some Data
# for i , embed_data in enumerate(text_embed):
#     print(f"Chunk No : {i+1} , Text Embedding Data : {embed_data[:5]}")
# # Check the Cosine Similarity Between Two Chunks
# if len(text_embed) >= 2:
#     print(f"Cosine Similarity of First & Second Chunk : {cosine_similarity([text_embed[0]] , [text_embed[1]])}")



# Part No 2 (LangChain OpenSource Embedding) --> OllamaEmbeddings --> https://python.langchain.com/api_reference/ollama/embeddings/langchain_ollama.embeddings.OllamaEmbeddings.html#

MODEL_NAME_EMB = "llama3.2"
# embedding      = OllamaEmbeddings(model = MODEL_NAME_EMB)

# # Convert the Doc into Embedding
# text_embed = embedding.embed_documents([chunk.page_content for chunk in doc])
# # Display the Chunk No & Embedding Some Data
# for i , embed_data in enumerate(text_embed):
#     print(f"Chunk No : {i+1} , Text Embedding Data : {embed_data[:5]}")
# # Check the Cosine Similarity Between Two Chunks
# if len(text_embed) >= 2:
#     print(f"Cosine Similarity of First & Second Chunk : {cosine_similarity([text_embed[0]] , [text_embed[1]])}")
