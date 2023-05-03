from django.db import models
from account.validator import validate_file_size,validate_picture_size
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from job.models.suggest import Key

User = get_user_model()

class UserProfile(models.Model):
    SEX = (
        ('مرد','مرد'),
        ('زن','زن'),
    )
    user = models.OneToOneField('User',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    picture = models.ImageField(validators=[validate_picture_size],blank=True,null=True)
    lastname = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    age = models.IntegerField(blank=True,null=True)
    sex = models.CharField(choices=SEX,default='مرد',max_length=10)

    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    code_posty = models.CharField(max_length=10)
    address = models.TextField(help_text='آدرس دقیق')

    tahsilat = models.CharField(max_length=400)
    info = models.TextField(null=True)
    key = models.ManyToManyField(Key,blank=True)
    cv_file = models.FileField(validators=[validate_file_size],null=True)
    linkedin = models.URLField(max_length=200,blank=True,null=True)
    wish_list = models.ManyToManyField('job.Job',blank=True)


    def __str__(self):
        return self.user.email + "/// " + self.lastname



@receiver(post_save, sender=User)
def profile_company_maker(sender,instance,created,**kwargs):
    if created and instance.employee:
        UserProfile.objects.create(user=instance)
