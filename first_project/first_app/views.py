from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.

# def index(request: HttpRequest):
#     return HttpResponse("Hello World!")

def index(request: HttpRequest) -> HttpResponse:
    index_tags = {"insert_me": "Hello I am from views.py"}
    return render(request, "first_app/index.html", context=index_tags)