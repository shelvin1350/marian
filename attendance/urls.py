
from django.urls import path
from attendance import  views

urlpatterns = [
   path('', views.attendance_register),
   path('index', views.index),
   path('attendance', views.attendance, name='attendance'),
   path('attendance/date', views.attendanceByDate, name='attendance/date'),
   path('attendance/date/view', views.viewByDate)
    
    
]
