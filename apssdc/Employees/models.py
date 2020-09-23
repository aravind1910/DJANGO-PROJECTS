from django.db import models

# Create your models here.
class EmpRegister(models.Model):
    genvalues=[('Male','Male'),('Female','Female')]
    deptvalues=[('HR','HR'),('Accounts','Accounts'),('R&D','R&D')]
    Emp_Firstname=models.CharField(max_length=50)
    Emp_Lastname=models.CharField(max_length=50)
    Emp_Age=models.IntegerField(null=False)
    Emp_Id=models.CharField(max_length=20)
    Emp_Gender=models.CharField(max_length=20,choices=genvalues)
    Emp_Email=models.EmailField(max_length=50)
    Emp_Password=models.CharField(max_length=20)
    Emp_Salary=models.FloatField(null=False)
    Emp_Department=models.CharField(max_length=30,choices=deptvalues)

    def __str__(self):
        return self.Emp_Email
        