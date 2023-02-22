from django.db import models
from account.validator import validate_file_size
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    SEX = (
        ('مرد','مرد'),
        ('زن','زن'),
    )
    user = models.OneToOneField('User',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    picture = models.ImageField()
    lastname = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    age = models.IntegerField()
    sex = models.CharField(choices=SEX,default='مرد',max_length=10)

    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    code_posty = models.CharField(max_length=10)
    address = models.TextField(help_text='آدرس دقیق')

    tahsilat = models.CharField(max_length=400)
    info = models.TextField()
    cv_file = models.FileField(validators=[validate_file_size])


    def __str__(self):
        return self.name + " " + self.lastname
