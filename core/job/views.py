from django.shortcuts import render
from .models.job import Job
from home.models import Slider

# Create your views here.
def listview(request):
    context = {
        'jobs':Job.objects.filter(status=True).order_by('-created'),
        'slider':Slider.objects.filter().last(),
    }
    return render(request,'listview.html',context)