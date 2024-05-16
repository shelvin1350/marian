from django.db import models

class Employees(models.Model):
    FirstName=models.CharField(max_length=250)
    LastName=models.CharField(max_length=250)
    DateOfBirth=models.DateField(default='NULL')
    Position=models.CharField(max_length=250, default='NULL')
    Email=models.CharField(max_length=250)
    PhoneNumber=models.CharField(max_length=50)
    
