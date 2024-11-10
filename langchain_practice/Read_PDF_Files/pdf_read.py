# Import the Important Modules
from langchain_community.document_loaders import PyPDFLoader


# Now Read the PDF File using PYPDF Loader
FILE_PATH = "../../PDF_Files/machine_learning_overview.pdf"
loader = PyPDFLoader(FILE_PATH)

# Load the PDF File
pages = loader.load()

# Display the Length of the Pages
print(f"Here is the Length of the Pages : {len(pages)}\n")

# Now Display the Meta Data of the First Page
print(f"Here is the Meta Data of the First Page : {pages[0].metadata}\n")

# Display the Page Content of the First Page
print(f"Here is the Page Conent of the First Page : \n{pages[0].page_content[:102]}\n")

# Now, Display the All Page Content of the First Page
print(f"Here is the All Page Content of First Page : \n{pages[0].page_content}")
