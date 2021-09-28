from django.urls import path
from django.urls.resolvers import URLPattern 
from .views import index, about
urlpatterns = [
    path('', index, name = "index"),
    path('about', about, name = "about"),
]