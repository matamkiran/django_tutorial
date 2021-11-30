from django.db import models

# Create your models here.
# Create your models here.
class EmployeeDemo(models.Model):
    
    name=models.TextField()
    gender=models.TextField(default='M')
    address=models.TextField(default='India')
    age=models.IntegerField
    salary=models.IntegerField


class SutdentDemo(models.Model):
    
    name=models.TextField()
    age=models.IntegerField
    fees=models.IntegerField
    qualification=models.CharField(max_length=20)