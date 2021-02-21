from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from basic_app.forms import UserForm, UserProfileInfoForm
from basic_app.models import UserProfileInfo

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request: "HttpRequest") -> HttpResponse:
    return render(request, "basic_app/index.html")

def register(request: "HttpRequest") -> HttpResponse:

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user: User = user_form.save()
            user.set_password(user.password)
            user.save()

            profile: UserProfileInfo = profile_form.save(commit=False) # To avoid saving to the database directly and perform operations before.
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "basic_app/registration.html",
                  {
                      "user_form": user_form,
                      "profile_form": profile_form,
                      "registered": registered
                  })

def special(request: "HttpRequest") -> HttpResponse:
    return HttpResponse("You're logged in, Nice!")

@login_required
def user_logout(request: "HttpRequest") -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def user_login(request: "HttpRequest") -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password {password}")
            return HttpResponse("Invalid login detailes supplied!")

    else:
        return render(request, "basic_app/login.html", {})