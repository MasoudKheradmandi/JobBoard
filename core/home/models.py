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
    
