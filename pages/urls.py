from django.urls import path
from .views import home_page_view


url_patterns = [
    # `name` is optional
    # if user requests home page represented in empty string, it will use `home_page_view`
    path('', home_page_view, name='home'),
]
