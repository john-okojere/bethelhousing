from django import template, views
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views 
from . import views 

urlpatterns = [
    path('', views.property_search, name="property-search" ),
    path('home/', views.home_property_search, name="home-property-search" ),
]
