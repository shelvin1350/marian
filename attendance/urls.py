
from django.urls import path
from attendance import  views

urlpatterns = [
   path('', views.attendance_register),
   path('index', views.index),
   path('attendance', views.attendance)
    
    
]
