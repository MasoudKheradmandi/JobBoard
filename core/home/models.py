from django.db import models

# Create your models here.
class Slider(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length=200)