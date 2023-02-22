from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# from .user import User

User = get_user_model()

class Company(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='company_user')
    logo = models.ImageField(blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=250,blank=True)
    date_foundations = models.CharField(max_length=200)
    locations = models.TextField(help_text='آدرس شرکت',blank=True)

    phone = models.CharField(max_length=13)
    ostan = models.CharField(max_length=200)
    city = models.CharField(max_length=250)

    info = models.TextField()
    code_posty = models.CharField(max_length=10,null=True)
    
    instagram = models.CharField(max_length=300,blank=True)
    linkedin = models.URLField(max_length=250,blank=True)
    facebook = models.URLField(max_length=250,blank=True,null=True)
    telegram = models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return (self.user.email) + "/  " + self.name


@receiver(post_save, sender=User)
def profile_company_maker(sender,instance,created,**kwargs):
    if created and instance.company:
        Company.objects.create(user=instance)
