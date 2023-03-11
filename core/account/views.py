from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login
from .models.user import User
from .models.company import Company
from .forms import CompanyForm,UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models.user_profile import UserProfile
import random
from django.http import HttpResponse




#--------------------Company--------

def company_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=User.objects.create_user(email=username,password=password,company=True)
        messages.success(request,'ثبت نام شما با موفقیت انجام شد!')
        login(request,user)
        return redirect('account:company_profile')


    return render(request,'company_login/register.html',)


    
def CompanyProfile(request):
    obj = Company.objects.get(user_id=request.user.id)
    
    if request.method == "POST":
        form = CompanyForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ذخیره شد')
            return redirect('/')
        else:
            messages.error(request,'اطلاعات وارد شده مورد تایید نمیباشد')
    form = CompanyForm(instance=obj)
    
    context = {
        "form":form,
    }
    return render(request,'company-profile.html',context)






#--------------------user--------------


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,'شما با موفقیت وارد حساب کاربری خود شدید')
            return redirect('home:home')
    form = AuthenticationForm()

    return render(request,'register.html',{'form':form})


def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            user=User.objects.create_user(email=username,password=password,employee=True)
            messages.success(request,'ثبت نام شما با موفقیت انجام شد!')
            login(request,user)
            return redirect('home:home')
        else:
            messages.error(request,'رمز های وارد شده یکسان نمیباشد')

    return render(request,'register.html',)


def user_profile(request):
    obj = UserProfile.objects.get(user_id=request.user.id)

    if request.method == "POST":
        form = UserProfileForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت ذخیره شد')
            return redirect('/')
        else:
            messages.error(request,'اطلاعات وارد شده مورد تایید نمیباشد')
    form = UserProfileForm(instance=obj)
    
    context = {
        "form":form,
        'obj':obj
    }
    return render(request,'user_profile.html',context)


def reset_token(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            User.objects.get(email=email)
            random_number = random.randint(1000,9999)
            user=User.objects.get(email=email)
            user.Token = random_number
            user.save()
            return redirect('account:send_mail')
        except:
            messages.error(request,'همچین اکانتی وجود ندارد')
            return HttpResponse("BUG")
        
def send_mail(request):
    pass