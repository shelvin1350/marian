from django.db import models

class Employees(models.Model):
    FirstName=models.CharField(max_length=250)
    LastName=models.CharField(max_length=250)
    DateOfBirth = models.DateField(default=None, null=True, blank=True)    
    Position=models.CharField(max_length=250, default='NULL')
    Email=models.CharField(max_length=250)
    PhoneNumber=models.CharField(max_length=50)
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    Date = models.DateField()
    ExtraHours = models.IntegerField(default=0)
    Forenoon = models.IntegerField(default=0)
    Afternoon = models.IntegerField(default=0)
    TotalHours = models.IntegerField(null=True, blank=True)  
    
