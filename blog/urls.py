from django.urls import path
from .views import BlogHomeView, BlogCreatePostView, BlogPostDetailView, BlogUpdatePostView, BlogDeletePostView


urlpatterns = [
    path("post/new/", BlogCreatePostView.as_view(), name="blog_new_post"),
    path("post/<int:pk>/", BlogPostDetailView.as_view(), name="blog_post_detail"),
    path("post/<int:pk>/edit/", BlogUpdatePostView.as_view(), name="blog_post_edit"),
    path("post/<int:pk>/delete/", BlogDeletePostView.as_view(), name="blog_post_delete"),
    path("", BlogHomeView.as_view(), name="bloghome")
]
