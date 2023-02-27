from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Slider





User = get_user_model()
# Create your views here.
def home(request):
    context = {
        'slider':Slider.objects.filter().last()
    }
    return render(request,'index.html',context)