from django.shortcuts import render
from .models.job import Job
from home.models import Slider
from django.core.paginator import Paginator


# Create your views here.
def listview(request):
    contact_list = Job.objects.filter(status=True).order_by('-created'),
    paginator = Paginator(contact_list, 25)
    
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'jobs':Job.objects.filter(status=True).order_by('-created'),
        'slider':Slider.objects.filter().last(),
    }
    return render(request,'listview.html',context)