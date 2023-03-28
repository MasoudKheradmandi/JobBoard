from django.db import models

# Create your models here.
class Slider(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length=200)

class NavOne(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام نوبار')
    link = models.CharField(max_length=100,verbose_name='لینک نوبار',blank=True)    
    def __str__(self):
        return self.name

class NavTwo(models.Model):
    parent = models.ForeignKey(NavOne,on_delete=models.PROTECT)
    name = models.CharField(max_length=100,verbose_name='نام نوبار')
    link = models.CharField(max_length=100,verbose_name='لینک نوبار')    
    def __str__(self):
        return self.name
    

class AboutUs(models.Model):
    banner = models.ImageField(null=True)
    title = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField()


    def __str__(self):
        return self.title
    


class ZirAboutUs(models.Model):
    banner = models.ImageField(null=True)
    title = models.CharField(max_length=250)
    zir_title = models.TextField()
    button_name = models.CharField(max_length=150)
    button_link = models.URLField()


class ContatctUs(models.Model):
    email = models.EmailField(max_length=254,unique=True)


    def __str__(self):
        return self.email
    

class HomeComment(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=150)
    image = models.ImageField()
    comment = models.TextField()
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.name
