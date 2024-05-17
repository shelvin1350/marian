from django.shortcuts import render
from django.http import HttpResponse
from . models import Employees

def index(request):
    return render(request,'index.html')

def attendance_register(request):
    data = Employees.objects.all()
    return render(request, 'attendance_register.html', {'details':data})

def attendance(request):
    if request.method == "POST":
        date = request.POST.get('date')
        morning_attendance = []
        afternoon_attendance = []

        employees = Employees.objects.all()
        for employee in employees:
            emp_id = employee.id
            morning_toggle = request.POST.get(f'morning_{emp_id}')
            afternoon_toggle = request.POST.get(f'afternoon_{emp_id}')
            is_present_m = morning_toggle == 'on'
            is_present_e = afternoon_toggle == 'on'

            morning_attendance.append((emp_id, is_present_m))
            afternoon_attendance.append((emp_id, is_present_e))

        print(f"Date is {date}")
        for emp_id, is_present_m in morning_attendance:
            total_hours=0
            print(f"Employee ID: {emp_id}, Morning Attendance: {'Present' if is_present_m else 'Absent'}")
            if(is_present_m):
                mr_hours=4
                total_hours=total_hours+mr_hours
        for emp_id, is_present_e in afternoon_attendance:
            print(f"Employee ID: {emp_id}, afternoon Attendance: {'Present' if is_present_e else 'Absent'}")
            if(is_present_e):
                mr_hours=4
                total_hours=total_hours+mr_hours
    data = Employees.objects.all()
    return render(request, 'attendance_register.html', {'details': data})
