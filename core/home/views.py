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
from resume.models import SendResume
from django.db.models import Count , Q
User = get_user_model()
# Create your views here.
def home(request):
    # x = JobCategory.objects.annotate(num_jobs=Count('job'),filter=Q(job__status=True)).order_by('-num_jobs')
    
    context = {
        'slider':Slider.objects.filter().last(),
        'jobs':Job.objects.filter(status=True).order_by('-created')[:5],
        'comments':HomeComment.objects.filter(status=True),
        'count_jobs':Job.objects.filter(status=True).count(),
        'category':JobCategory.objects.filter(job__status=True).annotate(num_jobs=Count('job')).order_by('-num_jobs'),
        'cat_count':JobCategory.objects.all().count(),
        'users':User.objects.filter(employee=True).count(),
        'resume_count':SendResume.objects.all().count(),
    }
    return render(request,'index.html',context)



def NavBar(request):
    context = {
        'NavOne':NavOne.objects.all(),
    }
    return render(request,'layout/header.html',context)

from faker import Faker

def aboutus(request):
    # fake = Faker('fa_IR')
    # key_list=[]
    # for l in Key.objects.all():
    #     key_list.append(l)
    # for number in range(100):
    #     company = []
    #     job_cat = []
        
    #     for x in Company.objects.all():
    #         company.append(x)
    #     for m in JobCategory.objects.all():
    #         job_cat.append(m)
    #     obj=Job.objects.create(
    #         company = fake.random_element(elements=company),name=fake.job(),category=fake.random_element(elements=job_cat),style=fake.random_element(elements=('تمام وقت', 'پاره وقت', 'کارآموز','فریلنسر')),
    #         experience=fake.random_element(elements=('1','2','3','4')),ostan=fake.random_element(elements=('گیلان','مازندران','آذربایجان شرقی','آذربایجان غربی','کرمانشاه')),salary=fake.random_int(min=2, max=100),info= fake.text(max_nb_chars=500),necessary= fake.paragraph(),privilege=fake.text(),status=fake.boolean(chance_of_getting_true=70),telecommuting=fake.boolean(chance_of_getting_true=20),created=fake.date_between(start_date='-30y', end_date='today'),updated_at=fake.date_between(start_date='-30y', end_date='today'),
    #     )
    # for job in Job.objects.all():
    #     random_tags = fake.random_elements(elements=key_list, length=fake.random_int(min=1, max=5))
    #     job.job_keys.add(*random_tags)
    # Job.objects.all().delete()
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
            if ContatctUs.objects.filter(email=email).exists():
                messages.error(request,'ایمیل شما قبلا ثبت شده')
                return redirect('home:home')
            else:
                ContatctUs.objects.create(email=email)
                messages.success(request,'ایمیل شما دریافت شد')
                return redirect('home:home')
        

# def sendmail(request):
#     email=send_mail(
#     str('subject'),
#     str('Here is the message.'),
#     'masoud1212u@gmail.com',
#     ['kheradmandimasoud416@gmail.com'],
#     )
#     email.send()
#     return HttpResponse("Done")

