from django.urls import re_path
from second_app import views

urlpatterns = [
    re_path(r"^$", views.index, name="index")
]