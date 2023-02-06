from django.urls import path, reverse_lazy
from . import views 

urlpatterns = [
    path('', views.home , name="homepage" ),
    path('about-us', views.about , name="about" ),
    path('FAQs', views.faq , name="faqs" ),
    path('contact-us', views.contact , name="contact" ),
]
