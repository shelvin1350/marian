
from django.urls import path
from attendance import  views

urlpatterns = [
   path('attendance/', views.attendance_register)
    
    
]
