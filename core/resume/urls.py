from django.urls import path

from . import views


urlpatterns = [
    path('get_resume/',views.get_resume,name='get_resume')
]
