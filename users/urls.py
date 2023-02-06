from django import template, views
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views 
from . import views 

urlpatterns = [
    path('Login/', LoginView.as_view(template_name="account/user-login.html"), name="login" ),
    path('Logout/', LogoutView.as_view(), name="logout" ),
    path('Sign-up/', views.signup , name="sign-up" ),
    path('myprofile/', views.profile , name="profile" ),
    path('updateaccount/<str:username>', views.updateaccount, name="updateaccount" ),

]
