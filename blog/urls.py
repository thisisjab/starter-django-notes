from django.urls import path
from .views import BlogHomeView, BlogPostDetailView


urlpatterns = [
    path("post/<int:pk>/", BlogPostDetailView.as_view(), name="blog_post_detail"),
    path("", BlogHomeView.as_view(), name="bloghome")
]
