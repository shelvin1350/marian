
from django.urls import path
from attendance import  views

urlpatterns = [
   path('', views.attendance_register),
   path('attendance', views.attendance, name='attendance'),
   path('attendance/date', views.attendanceByDate, name='attendance/date'),
   path('attendance/date/view', views.view_employee_details),
   path('attendance/date/view/<int:employee_id>', views.view_employee_details, name='view_employee_details'),
   path('attendance/employee/<int:employee_id>/', views.view_employee_attendance, name='employee_attendance'),

    
]
