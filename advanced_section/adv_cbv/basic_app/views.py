from typing import Dict, Any

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest
from basic_app import models


# Create your views here.

# function type view

# def index(request):
#     return render(request, "index.html")


# class type view

# Replying a simple http response

# class CBView(View):
#     def get(self, request: HttpRequest) -> HttpResponse:
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["injected_content"] = "BASIC INJECTION!"
        return context


class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School
    # returns a list with the name of school_list if context_object_name is not specified


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
