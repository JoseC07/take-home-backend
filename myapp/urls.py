from django.urls import path
from .views import  calculate, send_email

urlpatterns = [
   
    
    path('calculate/', calculate, name='calculate'),
    path('send-email/', send_email, name='send-email'),
   
]
