from django.contrib import admin

from .models.job import Job,JobCategory


admin.site.register(Job)

admin.site.register(JobCategory)