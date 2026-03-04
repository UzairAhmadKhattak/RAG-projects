
# 1) load the resume using lanchain pdf loader
# 2) split the resume into chunks
# 3) embed the chunks using the openai embedding model
# 4) store the chunks in a postgres vector table
# ... more steps in the quering_db folder

from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# load the resume
def function_load_pdf():
    resume_file_name = os.getenv("resume_file_name")
    loader = PyPDFLoader(os.path.join(os.path.dirname(__file__), resume_file_name))
    return loader.load()

# split the resume into chunks
def function_split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def return_vector_store(pre_delete_collection=False):
    return PGVector(
        embeddings=OpenAIEmbeddings(model="text-embedding-3-small", api_key=os.getenv("openai_api_key")),
        collection_name=os.getenv("collection_name"),
        connection=os.getenv("database_url"),
        pre_delete_collection=pre_delete_collection,
    )


if __name__ == "__main__":
    # convert documents to embeddings and add to the vector store
    docs = function_load_pdf()
    split_docs = function_split_documents(docs)
    vector_store = return_vector_store(pre_delete_collection=True)
    vector_store.add_documents(split_docs)