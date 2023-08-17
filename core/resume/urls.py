from django.urls import path

from . import views

app_name='resume'

urlpatterns = [
    path('get_resume/',views.get_resume,name='get_resume'),
    path('delete/<int:id>/',views.delete_cv,name='delete_cv'),
    path('readme/',views.readme,name='readme')
]
