from document_loaders import documentLoaders
from config import *

def load_content(file_path, file_extension=None):
    loader = documentLoaders(file_path) # Create a document loader object
    if file_extension == "pdf":
        file_content = loader.load_pdf_using_pymupdf() #extract the content of pdf file from pymupdf loader
    elif file_extension == "csv":
        file_content = loader.load_csv() #extract the content of csv file from CSV loader
    elif file_extension == "png":
        file_content = loader.load_image()
    return file_content

def main():
    supported_files = ["pdf", "csv", "png"]
    file_index = int(input("Enter 1 to select a pdf file. \nEnter 2 to select a csv file. \nEnter 3 to select a image file. \nNumber: ")) 
    if file_index == 1:
        file_path = PDF_FILE_PATH
    elif file_index == 2:
        file_path = CSV_FILE_PATH
    elif file_index == 3:
        file_path = PNG_FILE_PATH 

    file_extension = file_path.split('\\')[-1].split(".")[-1] #extract the file extension e.g. pdf from the file path
    if file_extension not in supported_files: #if the file extension is not lie in supported files list, then return exception
        return("This file is not supported at the moment.")
    """
    Load the file content
    """
    file_content = load_content(CSV_FILE_PATH, file_extension)
    print(file_content)


if __name__ == "__main__":
    main()
