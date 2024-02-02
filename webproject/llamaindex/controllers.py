import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

from llama_index import VectorStoreIndex, SimpleDirectoryReader

def load_documents():
    directory = "/Users/andreluiz/python-projects/llms-django-llamaindex/webproject/data"
    documents = SimpleDirectoryReader(directory).load_data()
    # index = VectorStoreIndex.from_documents(documents)
    return documents