from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .models import Slider
from job.models.job import Job
from .models import NavOne,AboutUs,ZirAboutUs,ContatctUs,HomeComment
from django.contrib import messages
from .forms import ContactUsForm
from django.core.mail import send_mail
from django.http import HttpResponse
from job.models import JobCategory
from django.db.models import Count , Q

User = get_user_model()
# Create your views here.
def home(request):
    x = JobCategory.objects.annotate(num_jobs=Count('job'),filter=Q(job__status=True)).order_by('-num_jobs')
    print(x)
    context = {
        'slider':Slider.objects.filter().last(),
        'jobs':Job.objects.filter(status=True).order_by('-created')[:5],
        'comments':HomeComment.objects.filter(status=True),
        'category':JobCategory.objects.filter(job__status=True).annotate(num_jobs=Count('job')).order_by('-num_jobs'),
        'cat_count':JobCategory.objects.all().count()
    }
    return render(request,'index.html',context)



def NavBar(request):
    context = {
        'NavOne':NavOne.objects.all(),
    }
    return render(request,'layout/header.html',context)


def aboutus(request):
    context = {
        'about_us':AboutUs.objects.filter().last(),
        'zir':ZirAboutUs.objects.filter().last(),
    }
    return render(request,'about-us.html',context)


def contactus(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            ContatctUs.objects.create(email=email)
            messages.success(request,'ایمیل شما دریافت شد')
            return redirect('home:home')
        

def sendmail(request):
    email=send_mail(
    str('subject'),
    str('Here is the message.'),
    'masoud1212u@gmail.com',
    ['kheradmandimasoud416@gmail.com'],
    )
    email.send()
    return HttpResponse("Done")