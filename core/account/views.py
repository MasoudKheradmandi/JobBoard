from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from .models.user import User
# Create your views here.

def SignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=User.objects.create_user(email=username,password=password,company=True)
        messages.success(request,'ثبت نام شما با موفقیت انجام شد!')
        login(request,user)
        pass


    return render(request,'company_login/register.html',)


    
