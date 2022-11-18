from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostsView(ListView):
    model = Post
    template_name = "posts.html"
