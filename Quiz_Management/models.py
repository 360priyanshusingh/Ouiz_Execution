from django.contrib.auth.models import User
from django.db import models


# Create your models here.



class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True ,blank=True )
    mobile_number = models.CharField(max_length=200, null=True, blank=True)
    joining_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    image=models.FileField(null=True, blank=True)
    salary=models.CharField(max_length=200, null=True, blank=True)
    status=models.CharField(max_length=200, null=True, blank=True)



class Branch(models.Model):
    branch_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.branch_name


class Courses(models.Model):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True,blank=True)
    courses_name = models.CharField(max_length=200, null=True, blank=True)
    total_question = models.CharField(max_length=200, null=True, blank=True)
    total_marks = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.courses_name
class Questions(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    question_name=models.CharField(max_length=200, null=True, blank=True)
    marks=models.CharField(max_length=200, null=True, blank=True)
    option1=models.CharField(max_length=200, null=True, blank=True)
    option2=models.CharField(max_length=200, null=True, blank=True)
    option3=models.CharField(max_length=200, null=True, blank=True)
    option4=models.CharField(max_length=200, null=True, blank=True)
    ans=models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.question_name


class Student(models.Model):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile_number = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    father_name= models.CharField(max_length=200, null=True, blank=True)
    father_email=models.CharField(max_length=200, null=True, blank=True)


class Quiz(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    marks = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)



class Assigncourses(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

