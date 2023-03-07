from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .models import Slider
from job.models.job import Job
from .models import NavOne,AboutUs,ZirAboutUs,ContatctUs
from django.contrib import messages
from .forms import ContactUsForm


User = get_user_model()
# Create your views here.
def home(request):
    context = {
        'slider':Slider.objects.filter().last(),
        'jobs':Job.objects.filter(status=True).order_by('-created'),
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