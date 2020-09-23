from django.shortcuts import render
from django.http import HttpResponse
from Student.models import *

# Create your views here.
def home(request):
    return HttpResponse("Welcome nemo")
def home1(request,name,id):
    return HttpResponse("<h1>Welcome {} my roll number is {}</h1>".format(name,id))
def home2(request):
    return render(request,"Student/home.html")
def register(request):
    if(request.method=="POST"):
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        age=request.POST["age"]
        email=request.POST["email"]
        tel=request.POST["tel"]
        gender=request.POST["gender"]
        password=request.POST["password"]
        data={'FName':fname,'LName':lname,'Age':age,'Email':email,'Mobile':tel,'Gender':gender,'Password':password}
        UserReg.objects.create(FName=fname,LName=lname,Age=age,Email=email,Mobile=tel,Gender=gender,Password=password)
        print(data)
        return HttpResponse("Registered Successfully!!")
    return render(request,'Student/index.html')
def login(request):
    if(request.method=="POST"):
        username=request.POST["email"]
        password=request.POST["password"]
        data=UserReg.objects.filter(Email=username)
        if(len(data)==0):
            return HttpResponse("Not registered Yet!!")
        else:
            data=UserReg.objects.get(Email=username)
            if(data.Password==password):
                return render(request,'Student/showdata.html',{'info':data})
            else:
                return HttpResponse("Wrong Password!!")
    return render(request,'Student/login.html')
d={'count':0}
def counter(request):
    if(request.method=="POST"):
        if request.POST.get("submit"):
            d['count']+=1
        if request.POST.get("reset"):
            d['count']=0
        print(d['count'])
        return render(request,'Student/counter.html',{'info':d})
    return render(request,'Student/counter.html',{'info':d})
def about(request):
    return render(request,'Student/about.html')

def FacDataShow(request):
    data=FacultyData.objects.all() #or FacultyData.objects.filter(FacName="Stephen")
    print(data)
    return render(request,'Student/facultydatashow.html',{'info':data})

def tables(request,id):
    data=[]
    for i in range(1,11):
        data.append(str(id)+' * '+str(i)+" = "+str(id*i))

    return render(request,'Student/tables.html',{'info':data,'num':i})



