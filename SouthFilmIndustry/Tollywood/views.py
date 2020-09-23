from django.shortcuts import render,redirect
from django.http import HttpResponse
from Tollywood.forms import *
from Tollywood.models import *
# Create your views here.

def index(request):
	return render(request,'Tollywood/index.html')

def register(request):
	if(request.method=="POST"):
		form=HeroForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/Tollywood/showdata')
		return redirect('/Tollywood/showdata')
	form=HeroForm()
	return render(request,'Tollywood/register.html',{'form':form})

def showdata(request):
	data=Heroregister.objects.all()
	print(data)
	return render(request,'Tollywood/showdata.html',{'data':data})

def edit(request,id):
	data=Heroregister.objects.get(id=id)
	if request.method=="POST":
		form=HeroForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/Tollywood/showdata')
	form=HeroForm(instance=data)
	return render(request,'Tollywood/edit.html',{"form":form,"data":data})

def edit2(request,id):
	data=Heroregister.objects.get(id=id)
	if request.method=="POST":
		form=HeroForm2(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/Tollywood/showdata')
	form=HeroForm2(instance=data)
	return render(request,'Tollywood/edit2.html',{"form":form,"data":data})
def delete(request,id):
	data=Heroregister.objects.get(id=id)
	data.delete()
	return redirect('/Tollywood/showdata')
def contact(request):
	if request.method=="POST":
		data=ContactForm(request.POST)
		data.save()
		redirect('/Tollywood/')
	form=ContactForm()
	return render(request,'Tollywood/contactform.html',{'form':form})
