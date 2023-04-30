from django.contrib import admin

from .models.job import Job,JobCategory
from .models.suggest import Key

admin.site.register(Job)

admin.site.register(JobCategory)
admin.site.register(Key)