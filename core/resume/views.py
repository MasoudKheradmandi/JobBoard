from django.shortcuts import render,get_object_or_404,redirect
from .forms import FormSender
from django.contrib.auth.decorators import login_required
from resume.models import SendResume
from account.models import User,Company
from django.contrib import messages

@login_required()
def get_resume(request):
    if request.user.company:
        company = Company.objects.get(user=request.user)
        resume=SendResume.objects.filter(reciver=company,status=True)
        # resume = SendResume.objects.filter(reciver=request.user)
        print(resume)
        context = {
            'CV_SEND':resume
        }
        return render(request,'get_resume.html',context)
    else:
        return render(request,'404.html')
    

def delete_cv(request,id):
    obj = get_object_or_404(SendResume,id=id)
    obj.status = False
    obj.save()
    messages.success(request,'درخواست از لیست شما حذف شد')
    return redirect('resume:get_resume')


def readme(request):
    return render(request,'readme.html',{})