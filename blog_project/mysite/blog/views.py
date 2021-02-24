from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import PostForm
from blog.models import Post, Comment


class AboutView(TemplateView):
    template_name = "about.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # with query set we basically make sort of sql query to our models.
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")


class PostDetailView(DetailView):
    model = Post


# We use a mixin here to required a user to be logged in for creating a post
# For that we implement multiple inheritance
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    # reverse_lazy waits until it is actually deleted to go to the success url
    success_url = reverse_lazy("post_list")


class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "blog/post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("created_date")