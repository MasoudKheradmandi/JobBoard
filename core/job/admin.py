from django.contrib import admin

from .models.job import Job,Ostan,JobCategory


admin.site.register(Job)
admin.site.register(Ostan)
admin.site.register(JobCategory)