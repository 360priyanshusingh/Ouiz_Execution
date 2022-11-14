from django import template

from Quiz_Management.models import *

register = template.Library()

@register.filter(name='obtainmarks')
def obtainmarks(data):
    q = Quiz.objects.filter(student__user=data)
    total = 0
    for i in q:
        total += int(i.marks)
    return total


@register.filter(name='totalmarks')
def totalmarks(data):
    student = Student.objects.get(user=data)
    q = Courses.objects.filter(branch_name=student.branch_name)
    total = 0
    for i in q:
        total += int(i.total_marks)
    return total

@register.simple_tag
def getpercent(total, obtain):
    percent = (int(obtain) * 100) / int(total)
    return percent
