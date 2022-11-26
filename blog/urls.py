from django.urls import path
from .views import BlogHomeView, BlogCreatePostView, BlogPostDetailView


urlpatterns = [
    path("post/new/", BlogCreatePostView.as_view(), name="blog_new_post"),
    path("post/<int:pk>/", BlogPostDetailView.as_view(), name="blog_post_detail"),
    path("", BlogHomeView.as_view(), name="bloghome")
]
