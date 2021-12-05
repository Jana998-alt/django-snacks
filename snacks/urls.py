from os import name
from django.urls import include
from django.urls.resolvers import URLPattern
from .views import AboutView, HomeView 
from django.urls import path


urlpatterns = [
    path('', HomeView.as_view() , name = "home" ),
    path('about', AboutView.as_view() , name = "about")
]

