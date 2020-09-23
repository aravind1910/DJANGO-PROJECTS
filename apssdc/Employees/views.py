from django.shortcuts import render,redirect
from django.http import HttpResponse
from Employees.models import *
# Create your views here.
def signup(request):
    if(request.method=="POST"):
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        email=request.POST['email']
        id=request.POST['id']
        salary=request.POST['salary']
        gender=request.POST['gender']
        dept=request.POST['dept']
        password=request.POST['password']
        data=EmpRegister(
            Emp_Firstname=fname,
            Emp_Lastname=lname,
            Emp_Age=age,
            Emp_Id=id,
            Emp_Gender=gender,
            Emp_Email=email,
            Emp_Password=password,
            Emp_Salary=salary,
            Emp_Department=dept,
        )
        data.save()
        return HttpResponse("Successfully Registered!!")
    return render(request,'Employees/signup.html')
def delete(request,id):
    obj=EmpRegister.objects.get(id=id)
    obj.delete()
    return redirect('/Employees/displaydata')

def edit(req,id):
    data=EmpRegister.objects.get(id=id)
    return render(req,'Employees/edit.html',{'obj':data})
def update(req,id):
    if req.method=="POST":
        fname=req.POST['fname']
        lname=req.POST['lname']
        age=req.POST['age']
        eid=req.POST['id']
        email=req.POST['email']
        salary=req.POST['salary']
        gender=req.POST['gender']
        department=req.POST['dept']
        epassword=req.POST['password']
        obj=EmpRegister.objects.filter(id=id).update(Emp_Firstname=fname,Emp_Lastname=lname,Emp_Age=age,Emp_Id=id,Emp_Gender=gender,Emp_Email=email,Emp_Password=epassword,Emp_Department=department,Emp_Salary=salary)
        return redirect('/Employees/displaydata')

def displaydata(request):
    data=EmpRegister.objects.all()
    return render(request,'Employees/showdata.html',{'info':data})