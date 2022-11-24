from django.views.generic import ListView
from .models import Post


class BlogHomeView(ListView):
    model = Post
    template_name = "bloghome.html"
