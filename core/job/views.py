from django.shortcuts import render
from account.models import UserProfile
from .models.job import Job
from home.models import Slider
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from account.models.user import User

# Create your views here.
def listview(request):
    contact_list = Job.objects.filter(status=True).order_by('-created')
    paginator = Paginator(contact_list, 1)
    
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'jobs':page_obj,
        'slider':Slider.objects.filter().last(),
    }
    return render(request,'listview.html',context)


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
    print(user.userprofile.wish_list.all())
    context = {
        'wish_list':user.userprofile.wish_list.all()
    }
    return render(request,'wishlist.html',context)