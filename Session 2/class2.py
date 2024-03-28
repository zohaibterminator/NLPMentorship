from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader

class document_loaders:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf_using_pypdf(self):
        try:
            loader = PyPDFLoader(self.file_path)
            pages = loader.load()
            return pages

        except Exception as e:
            print(f"Error: {e}")    

    def load_pdf_using_pymupdf(self):
        try:
            loader = PyMuPDFLoader(self.file_path)
            data = loader.load()
            return data
 
        except Exception as e:
            print(f"Error: {e}")

dl = document_loaders(r"C:\Users\shahe\OneDrive\Desktop\NLP Sessions\Session 2\sensors-22-08281-v3.pdf")
pypdf_results = dl.load_pdf_using_pypdf()

pymupdf_results = dl.load_pdf_using_pymupdf()
print(pymupdf_results)