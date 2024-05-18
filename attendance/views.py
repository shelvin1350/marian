import random
from django.shortcuts import redirect, render
from django.http import HttpResponse
from faker import Faker
from django.db import transaction
from . models import Employees,Attendance


def index(request):
    return render(request,'index.html')

def attendance_register(request):
    data = Employees.objects.all()
    # faker = Faker()
    # positions = ['Manager', 'Developer', 'Designer', 'QA', 'DevOps', 'HR', 'Sales', 'Support']
    
    # for _ in range(50):
    #     first_name = faker.first_name()
    #     last_name = faker.last_name()
    #     date_of_birth = faker.date_of_birth(minimum_age=22, maximum_age=65)
    #     position = random.choice(positions)
    #     email = faker.email()
    #     phone_number = faker.phone_number()

    #     Employees.objects.create(
    #         FirstName=first_name,
    #         LastName=last_name,
    #         DateOfBirth=date_of_birth,
    #         Position=position,
    #         Email=email,
    #         PhoneNumber=phone_number
    #     )
    
    return render(request, 'attendance_register.html', {'details':data})

def attendance(request):
    if request.method == "POST":
        date = request.POST.get('date')
        if not date:
            # Handle missing date error
            return redirect('attendance')

        attendance_list = []

        employees = Employees.objects.all()
        for employee in employees:
            emp_id = employee.id
            first_name = employee.FirstName
            last_name = employee.LastName
            morning_toggle = request.POST.get(f'morning_{emp_id}') == 'on'
            afternoon_toggle = request.POST.get(f'afternoon_{emp_id}') == 'on'
            working_toggle = request.POST.get('working') == 'on'
            extra_hours = request.POST.get(f'extra_hours_{emp_id}', 0)
            extra_hours = float(extra_hours) if extra_hours else 0

            attendance_list.append({
                'emp_id': emp_id,
                'first_name': first_name,
                'last_name': last_name,
                'is_present_m': morning_toggle,
                'is_present_e': afternoon_toggle,
                'extra_hours': extra_hours
            })

        if working_toggle:
            print(f"Date is {date}")
            try:
                with transaction.atomic():
                    for attendance in attendance_list:
                        emp_id = attendance['emp_id']
                        is_present_m = attendance['is_present_m']
                        is_present_e = attendance['is_present_e']
                        extra_hours = attendance['extra_hours']

                        total_hours = (4 if is_present_m else 0) + (4 if is_present_e else 0) + extra_hours
                        date_id_obj = Attendance(
                            employee_id=emp_id,
                            Date=date,
                            Forenoon=4 if is_present_m else 0,
                            Afternoon=4 if is_present_e else 0,
                            ExtraHours=extra_hours,
                            TotalHours=total_hours
                        )
                        date_id_obj.save()

                        print(f"{attendance['first_name']} {attendance['last_name']}")
                        print(f"Morning Attendance: {'Present' if is_present_m else 'Absent'}")
                        print(f"Afternoon Attendance: {'Present' if is_present_e else 'Absent'}")
                        print(f'Total hours present = {total_hours}')
                        print(f'Extra hours present = {extra_hours}')
            except Exception as e:
                # Handle the exception (log it, notify, etc.)
                print(f"Error saving attendance: {e}")
                return redirect('attendance')

    data = Employees.objects.all()
    return render(request, 'attendance_register.html', {'details': data})


def attendanceByDate(request):
    data = Employees.objects.all()
    return render(request, 'attendance_date.html', {'details': data})

def viewByDate(request):
    return render(request, 'attendance_date_view.html')
    