from django.db import models
from account.models.company import Company
from django.utils import timezone
from datetime import datetime
from .suggest import Key

class JobCategory(models.Model):
    image = models.ImageField(blank=True,null=True)
    name = models.CharField(max_length=100)
    class_icon = models.CharField(max_length=100,null=True)

    
    def __str__(self):
        return self.name




class Job(models.Model):
    OSTAN_CHOICES = (
    ('گیلان','گیلان'),('مازندران','مازندران'),('آذربایجان شرقی','آذربایجان شرقی'),('آذربایجان غربی','آذربایجان غربی'),('کرمانشاه','کرمانشاه'),('خوزستان','خوزستان'),('فارس','فارس'),('کرمان','کرمان'),('خراسان','خراسان'),('اصفهان','اصفهان'),('سیستان و بلوچستان','سیستان و بلوچستان'),('کردستان','کردستان'),('همدان','همدان'),('چهارمحال و بختیاری','چهارمحال و بختیاری'),('لرستان','لرستان'),('ایلام','ایلام'),('کهگیلویه و بویراحمد','کهگیلویه و بویراحمد'),('بوشهر','بوشهر'),('زنجان','زنجان'),('سمنان','سمنان'),('یزد','یزد'),('هرمزگان','هرمزگان'),('تهران','تهران'),('اردبیل','اردبیل'),('قم','قم'),('قزوین','قزوین'),('گلستان','گلستان'),('خراسان شمالی','خراسان شمالی'),('خراسان جنوبی','خراسان جنوبی'),('البرز','البرز'),('مرکزی','مرکزی'),
    )
    STYLE = (
        ('تمام وقت','تمام وقت'),
        ('پاره وقت','پاره وقت'),
        ('کارآموز','کارآموز'),
        ('فریلنسر','فریلنسر')
    )
    EXPERIENCE = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='usercompany',null=True)
    name = models.CharField(max_length=400)
    category = models.ForeignKey(JobCategory,on_delete=models.CASCADE,null=True)
    style = models.CharField(max_length=20,choices=STYLE)
    experience = models.CharField(max_length=2,choices=EXPERIENCE)
    ostan = models.CharField(max_length=30,choices=OSTAN_CHOICES,null=True)
    salary = models.CharField(max_length=3,help_text='به میلیون بنویسید')
    info = models.TextField()
    necessary = models.TextField(verbose_name='مهارت های ضروری')
    privilege = models.TextField(blank=True,null=True,verbose_name='مهارت های امتیازی')
    
    status = models.BooleanField(default=False)
    job_keys = models.ManyToManyField(Key)
    telecommuting = models.BooleanField(default=False,verbose_name='امکان دورکاری')

    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

    @property
    def days_passed(self):
        today = datetime.now(timezone.utc)
        days_passed = today - self.created
        return f"{days_passed.days} روز پیش" if days_passed.days != 0 else 'امروز'
    
    def days_passed2(self):
        today = datetime.now(timezone.utc)
        days_passed = today - self.created
        return days_passed.days