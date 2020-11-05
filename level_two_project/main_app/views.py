from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from main_app.models import User

# Create your views here.
def index(request):
    return render(request, "main_app/index.html")

def users(request: HttpRequest) -> HttpResponse:
    users_list = User.objects.order_by("first_name")
    users_dict = {"users_list": users_list}
    return render(request, "main_app/users.html", context=users_dict)