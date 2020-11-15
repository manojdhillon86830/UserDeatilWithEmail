from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from taskapp import models
from taskproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def detail(request):
    res = render(request,'task.html')
    return res

def add(request):
    if request.method == 'POST':
        task = models.Content()
        task.name=request.POST['Name']
        task.Email=request.POST['email']
        task.phone=request.POST['Phone Number']
        task.Date_of_Birth=request.POST['Date of Birth']
        task.save()
        return HttpResponseRedirect('email')

def viewTask(request):
    content = models.Content.objects.all()
    res=render(request,'view_task.html', {'content':content})
    return res

def Email(request): 
    send_mail(
        'Thank You',
        'I have received your message and would like to thanku for giving me the details. Have a great day!',
        '21514manojkumar@gmail.com',
        ['manojsingh86830@gmail.com'],
        fail_silently=False,
        )
    return HttpResponseRedirect('view-task')
    

