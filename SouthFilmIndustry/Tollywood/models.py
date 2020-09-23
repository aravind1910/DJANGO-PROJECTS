from django.db import models
from django import forms

# Create your models here.
class Heroregister(models.Model):
	gender=[('Male','Male'),('Female','Female')]
	roles=[('Action','Action'),('Comedy','Comedy'),('Horror','Horror'),('Romance','Romance')]
	heroname=models.CharField(max_length=100)
	heroage=models.IntegerField(null=False,default=25)
	herogender=models.CharField(max_length=20,choices=gender)
	heroroles=models.CharField(max_length=40,choices=roles)
	herofilmcount=models.IntegerField(null=False,default=0)
	heroemail=models.EmailField(max_length=100)
	heroimage=models.ImageField(upload_to='hero_profiles/',null=False)
	heroautograph=models.ImageField(upload_to='hero_autographs/',null=False)
	def __str__(self):
		return self.heroname

class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	message=models.TextField(max_length=500)
	def __str__(self):
		return self.name

