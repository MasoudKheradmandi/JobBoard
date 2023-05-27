from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from .models.user import User
from .models.company import Company
from .forms import CompanyForm,UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models.user_profile import UserProfile
import random
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from job.models.job import Job
from django.db.models import Count
from django.core.paginator import Paginator
from account.decorators import is_company,is_employee
#--------------------Company--------

def company_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            user=User.objects.create_user(email=username,password=password,company=True)
            messages.success(request,'ثبت نام شما با موفقیت انجام شد!')
            login(request,user)
            return redirect('account:company_profile')
        else:
            messages.error(request,'پسووردهای وارد شده یکسان نمیباشد')

    return render(request,'company_login/register.html',)


@is_company
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

@is_employee
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
        if User.objects.filter(email=email):
            random_number = random.randint(1000,9999)
            user=User.objects.get(email=email)
            user.Token = random_number
            # send_mail(
            #     'فراوشی رمز عبور',
            #     f'{random_number}',
            #     'masoud1212u@gmail.com',
            #     [email],
            # )
            print(random_number)
            user.save()
            response = redirect('account:verify')
            response.set_cookie('email',email,1000)
            return response
            # return redirect('account:send_mail').set_cookie("Email",email,1000)
    else:
        messages.error(request,'همچین اکانتی وجود ندارد')
        return HttpResponse("BUG")


def verify(request):
    if request.method == "POST":
        token = request.POST.get('token')
        try:
            email = request.COOKIES['email']
            user=User.objects.get(email=email)

            if user.Token == int(token):
                login(request,user)
                return redirect('account:new_password')
            """
            میخوام بعد گرفتن توکن کاربرو ببرم صفحه ایی که برای خودش پسوورد ست کنه
            فقط باید بعد گرفتن توکن باید پسوورد جدید رو اپدیت کنه
            
            شاید هم برم برای ارسال کد چهاررقمی به کاربر

            """
        except:
            return HttpResponse("دوباره تلاش کنید")

    return render(request,'company_login/tokeninput.html',{})

@login_required
def new_password(request):
    if request.method == "POST":
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2 :
            user = request.user
            user.password = make_password(pass1)
            user.save()
            return HttpResponse("Success")
    return render(request,'changepass.html')

@is_employee
def suggest_job_for_user(request):
    keys = request.user.userprofile.key.all()
    job_suggestions = Job.objects.filter(job_keys__title__in=list(keys))
    job_suggestions = job_suggestions.annotate(s_count=Count('job_keys')).order_by('-s_count','-created')
    paginator = Paginator(job_suggestions, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context ={
        'jobs':page_obj
    }
    return render(request,'suggest.html',context)


def log_out(request):
    logout(request)
    messages.success(request,"شما با موفقیت از حساب کاربری خود خارج شدید")
    return redirect('/')