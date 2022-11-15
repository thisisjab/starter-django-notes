from django.urls import path
from .views import home_page_view, HomePageView


urlpatterns = [
    # `name` is optional
    # if user requests home page represented in empty string, it will use `home_page_view`
    path('', HomePageView.as_view(), name='home'),
]
