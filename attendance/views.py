from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def attendance_register(request):
    return render(request, 'attendance_register.html')