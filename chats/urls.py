from django import template, views
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views 
from . import views 

urlpatterns = [
    path('<int:pk>', views.sendmessage , name="sendmessage" ),
    path('message/<int:pk>', views.messages , name="message" ),
    path('unreadMessage/', views.get_unread_messages, name="unreadmessage" ),
    path('unreadSomeoneMessage/<int:pk>', views.get_someone_unread_messages, name="unreadsomeonemessage" ),

]
