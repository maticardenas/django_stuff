from django.urls import re_path
from main_app import views

urlpatterns = [
    re_path(r"users/", views.users, name="users")
]