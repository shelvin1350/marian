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
    Forenoon = models.FloatField(default=0)
    Afternoon = models.FloatField(default=0)
    ExtraHours = models.FloatField(default=0)
    TotalHours = models.FloatField(null=True, blank=True)  
    
