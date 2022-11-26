from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = "bloghome.html"


class BlogPostDetailView(DetailView):
    model = Post
    template_name = "blogpost.html"
    # context_object_name = "post" or "object"
    # You can use `context_object_name` to specify a custom name for this context


class BlogCreatePostView(CreateView):
    model = Post
    template_name = "blogcreate.html"
    fields = ["title", "author", "body"]
