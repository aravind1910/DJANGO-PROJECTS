from django.db import models

# Create your models here.
class StudentsData(models.Model):
    StuName=models.CharField(max_length=100)
    StuAge=models.IntegerField(null=False)
    StuEmail=models.EmailField(max_length=100,null=False)
    StuRoll=models.CharField(max_length=20)
    StuPassword=models.CharField(max_length=20)

class FacultyData(models.Model):
    FacName=models.CharField(max_length=100)
    FacAge=models.IntegerField(null=False)
    FacEmail=models.EmailField(max_length=100,null=False)
    FacID=models.CharField(max_length=20)

    def __str__(self):
        return self.FacName+' '+self.FacEmail+' '+self.FacID

class UserReg(models.Model):
    FName=models.CharField(max_length=100)
    LName=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,null=False)
    Age=models.IntegerField(null=False)
    Mobile=models.IntegerField(null=False)
    Gender=models.CharField(max_length=6)
    Password=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.FName+" "+self.LName
