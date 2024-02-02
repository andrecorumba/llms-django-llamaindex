from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from .controllers import load_documents

import os
from dotenv import load_dotenv, find_dotenv

from llama_index import VectorStoreIndex, SimpleDirectoryReader

load_dotenv(find_dotenv())

# Create your views here.
def index(request):
    return HttpResponse("Here is the index of the llamaindex app.")

def about(request):
    return JsonResponse({"response":"Here is the about page of the llamaindex app."})

def documents(request):
    # documents = load_documents()
    
    directory = "/Users/andreluiz/python-projects/llms-django-llamaindex/webproject/data"
    documents = SimpleDirectoryReader(directory).load_data()
    index = VectorStoreIndex.from_documents(documents)
    return JsonResponse({"response": str(documents)})