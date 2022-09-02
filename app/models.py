from distutils.command.upload import upload
from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    Department_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Department_Name

  


class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Address = models.CharField(max_length=255)
    Gender = models.CharField(max_length=10)
    DOB = models.DateField()
    Category_Name = (
        ('Trainee','Trainee'),
        ('Trainer','Trainer'),
        ('Employee','Employee'),
        ('Staff','Staff'),

    )
    Category_Name =models.CharField(max_length=150,choices=Category_Name,default='Trainee')
    State = models.CharField(max_length=50)
    Postcode = models.IntegerField()
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=100)
    mobile_number =models.IntegerField()
    Image = models.ImageField(upload_to='Profile_pic',null=True)
    Plus_two =models.ImageField(upload_to='Plus_two',null=True)
    Degree = models.ImageField(upload_to='Degree',null=True)
    Pg = models.ImageField(upload_to='Pg',null=True)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    
class Task (models.Model):
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Task_name = models.CharField(max_length=100)
    Start_date = models.DateField()
    End_date = models.DateField()

    def __str__(self):
        return self.Task_name

class User_task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Task = models.ForeignKey(Task,on_delete=models.CASCADE)

class Assigned_Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Task = models.ForeignKey(Task,on_delete=models.CASCADE)
    Description = models.CharField(max_length=255)
    File = models.FileField(upload_to='Task',null=True)
    Submition_Date = models.DateField(auto_now_add=True)

    Progress = (
        ('Pending','Pending'),
        ('Success','Success'),
        

    )
    Progress =models.CharField(max_length=150,choices=Progress,default='Pending')




    
class Topic (models.Model):
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Topic_name = models.CharField(max_length=100)
    Start_date = models.DateField()
    End_date = models.DateField()
    status = (
        ('Now','Now'),
        ('Review','Review'),
        

    )
    status =models.CharField(max_length=150,choices=status,default='Now')


    def __str__(self):
        return self.Topic_name


class Previous_Topic(models.Model):

    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Topic_name = models.CharField(max_length=100)
    Start_date = models.DateField()
    
    status = (
        ('Now','Now'),
        ('Review','Review'),
        

    )
    status =models.CharField(max_length=150,choices=status,default='Review')

    def __str__(self):
        return self.Topic_name



class Attendance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateField()
    status = (
        ('Present','Present'),
        ('Absent','Absent'),
        

    )
    status =models.CharField(max_length=150,choices=status,default='Absent')

    def __str__(self):
        return self.user.first_name



class Report(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    To = models.CharField(max_length=100)
    Report = models.CharField(max_length=255)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
   

    status = (
        ('Pending','Pending'),
        ('Updated','Updated'),
        

    )
    status =models.CharField(max_length=150,choices=status,default='Pending')

    def __str__(self):
        return self.user.first_name



class Payment(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)    
      Department = models.ForeignKey(Department,on_delete=models.CASCADE)
      Amount = models.IntegerField()
      Payment_Date = models.DateField()
      File = models.FileField(upload_to='Payment',null=True)

      def __str__(self):
        return self.user.first_name


class Leave(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    From = models.DateField()
    To = models.DateField()
    Leave = models.CharField(max_length=100)
    Reason = models.CharField(max_length=255)

    status = (
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
        

    )
    status =models.CharField(max_length=150,choices=status,default='Pending')


    def __str__(self):
        return self.user.first_name











    


