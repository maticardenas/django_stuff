from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    index_tags = {"insert_content": "Hello I am from second_app views!"}
    return render(request, "second_app/index.html", context=index_tags)