# Import the Important Modules 
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# Define the Model for the Embeding
MODEL_NAME = "all-MiniLM-L6-v2"
embedding  = HuggingFaceEmbeddings(model_name = MODEL_NAME)

# Define the document
doc = ["My Name is Usama" , "This is FAISS" , "Hello, How are you" , "My Age is 24" , "FAISS is a langchain module"]

# Define the Vector 
vector = FAISS.from_texts(doc , embedding)
retriever = vector.as_retriever(search_type = "similarity" , k = 1)

# Now Fetch the Data from the Retriever Vector DataBase
query = "what is FAISS"
answer = retriever.invoke(query)

# Display the Answer
print(answer)
