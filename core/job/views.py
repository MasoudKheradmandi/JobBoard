from django.shortcuts import render,get_object_or_404,redirect
from account.models import UserProfile
from .models.job import Job,JobCategory
from home.models import Slider
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import F
from account.models.user import User
from django.utils import timezone
from datetime import datetime
from resume.forms import FormSender
from django.contrib import messages

from resume.models import SendResume
# Create your views here.
def listview(request):

    contact_list = Job.objects.filter(status=True).order_by('-created')
    time = 90
    if request.GET.get('time'):
        time = request.GET.get('time')
        time_dict = {
            '3day':3,
            '3month':90,
            'week':7,
            'amonth':30,
        }
        contact_list=contact_list.annotate(days_passed3 =(datetime.now(timezone.utc).day-F('created__day'))).filter(days_passed3__lte=time_dict[time])

    paginator = Paginator(contact_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs':page_obj,
        'slider':Slider.objects.filter().last(),
        'time':time,
        'categorys':JobCategory.objects.all(),
    }
    return render(request,'listview.html',context)


def detailview(request,id):
    job = get_object_or_404(Job,id=id)
    form = FormSender()
    if request.method == "POST":
        if SendResume.objects.filter(reciver=job.company,sender=request.user,post=job):
            messages.error(request,'شما قبلا رزومه برای این شرکت فرستادید')
        else:
            form = FormSender(request.POST,request.FILES)
            if form.is_valid():
                reciver = job.company
                sender = request.user
                cv_file = form.cleaned_data['cv_file']
                SendResume.objects.create(reciver=reciver,sender=sender,post=job,cv_file=cv_file)
                messages.success(request,'رزومه شما با موفقیت ارسال شد')

    context = {
        'job':job,
        'form':form
    }
    return render(request,'job_detail.html',context)



def add_product_wish_list(request):

    profile=UserProfile.objects.get(user_id=request.user.id)
    obj = Job.objects.get(id=request.GET.get('id'))
    if obj in profile.wish_list.all():
        profile.wish_list.remove(obj)

    else:
        profile.wish_list.add(obj)

    return JsonResponse({'status':'success'})


@login_required
def wish_list(request):
    user = User.objects.get(id=1)
    wish_list = user.userprofile.wish_list.all()
    time = 90
    if request.GET.get('time'):
        time = request.GET.get('time')
        time_dict = {
            '3day':3,
            '3month':90,
            'week':7,
            'amonth':30,
        }
        wish_list=wish_list.annotate(days_passed3 =(datetime.now(timezone.utc).day-F('created__day'))).filter(days_passed3__lte=time_dict[time])
    paginator = Paginator(wish_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'wish_list':page_obj,
        'time':time
    }
    return render(request,'wishlist.html',context)


@login_required
def delete_from_wish_list(request,id):    
    obj = request.user.userprofile.wish_list.get(id=id)
    request.user.userprofile.wish_list.remove(obj)
    print(obj.__class__)
    return redirect('job:wish_list')



def searchlistview(request):
    name = request.GET.get('name')
    ostan = request.GET.get('ostan')
    category = request.GET.get('category')

    jobs = Job.objects.filter(status=True,name__contains=name,ostan__contains=ostan,category__name__contains=category).order_by('-created')
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs':page_obj,
        'paginator':paginator,
        'name':name,
        'ostan':ostan,
        'category':category,
        'categorys':JobCategory.objects.all(),
    }

    return render(request,'search_list_view.html',context)
