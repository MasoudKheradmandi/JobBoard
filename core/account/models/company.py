from django.db import models
from django.contrib.auth import get_user_model
# from .user import User

User = get_user_model()

class Company(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='company_user')
    logo = models.ImageField(blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=250,blank=True)
    date_foundations = models.CharField(max_length=200)
    locations = models.CharField(max_length=450,help_text='آدرس شرکت',blank=True)

    phone = models.CharField(max_length=13)
    ostan = models.CharField(max_length=200)
    city = models.CharField(max_length=250)

    info = models.TextField()

    instagram = models.CharField(max_length=300,blank=True)
    linkedin = models.URLField(max_length=250,blank=True)


    def __str__(self):
        return self.name