from django.shortcuts import render
from .forms import FormSender
from django.contrib.auth.decorators import login_required
from resume.models import SendResume
from account.models import User,Company


@login_required()
def get_resume(request):
    if request.user.company:
        company = Company.objects.get(user=request.user)
        resume=SendResume.objects.filter(reciver=company)
        # resume = SendResume.objects.filter(reciver=request.user)
        print(resume)
        context = {
            'CV_SEND':resume
        }
        return render(request,'get_resume.html',context)
    else:
        return render(request,'404.html')
    