import random
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from faker import Faker
from django.db import transaction
from . models import Employees,Attendance
from django.views.decorators.csrf import csrf_protect


def index(request):
    return render(request,'index.html')

def attendance_register(request):
    date = request.GET.get('date')
    exist = False
    if date:
        existing_records = Attendance.objects.filter(Date=date)
        if existing_records.exists():
            print(date)
            exist=True
    data = Employees.objects.all()
    return render(request, 'attendance_register.html',  {'e': exist, 'details': data})

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
    return render(request, 'attendance_date.html', {'details':data})

@csrf_protect
def view_employee_details(request, employee_id):
    # Retrieve the employee details based on the ID
    employee = get_object_or_404(Employees, id=employee_id)
    return render(request, 'attendance_date_view.html', {'employee': employee})
    
    
def view_employee_attendance(request, employee_id):
    if request.method == 'POST' and request.is_ajax():
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')

        # Query the attendance records for the employee within the specified date range
        attendance_data = Attendance.objects.filter(
            employee_id=employee_id,
            Date__range=[date_from, date_to]
        ).values('Date', 'Forenoon', 'Afternoon', 'ExtraHours', 'TotalHours')

        # Prepare the data to be sent as JSON response
        attendance_list = []
        for attendance in attendance_data:
            attendance_list.append({
                'date': attendance['Date'],
                'forenoon': attendance['Forenoon'],
                'afternoon': attendance['Afternoon'],
                'extra_hours': attendance['ExtraHours'],
                'total_hours': attendance['TotalHours']
            })

        return JsonResponse({'attendance_data': attendance_list})

    # If not a POST request or not an AJAX request, return 404
    return JsonResponse({'error': 'Page not found'}, status=404)