from django.shortcuts import render
from .models import EmployeeDemo
from .models import Employee

# Create your views here.

# Create your views here.
from django.http import HttpResponse

#import psycopg2
#from psycopg2 import Error
# Create your views here.

def home(request): 

    return render(request,'home.html')
    #return HttpResponse("<h1>hellooooooworld!!!!!!!!!!!!!!!!!!!!!!! its yoy first django statement</h1>")

def add(request):
    var1=request.POST["num1"]
    var2=request.POST["num2"]
    var3=request.POST["addr"]
    myObj=EmployeeDemo(name=var1,gender=var2,address=var3)
    myObj.save()
    allObj=EmployeeDemo.objects.all()
    return render(request,'result.html',{'result':allObj})

def addemp(request):
    var1=request.POST["name"]
    var2=request.POST["gender"]
    var3=request.POST["address"]
    var4=request.POST["age"]
    var5=request.POST["sal"]
    myObj=Employee(name=var1,gender=var2,address=var3,age=var4,salary=var5)
    myObj.save()
    allObj=Employee.objects.all()
    return render(request,'result.html',{'result':allObj})