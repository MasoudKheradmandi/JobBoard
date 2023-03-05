from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Slider
from job.models.job import Job
from .models import NavOne




User = get_user_model()
# Create your views here.
def home(request):
    context = {
        'slider':Slider.objects.filter().last(),
        'jobs':Job.objects.filter(status=True)
    }
    return render(request,'index.html',context)


def NavBar(request):
    context = {
        'NavOne':NavOne.objects.all(),
    }
    return render(request,'layout/header.html',context)