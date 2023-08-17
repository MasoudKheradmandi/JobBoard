from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.home,name='home'),
    path('header/',views.NavBar,name='header'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    # path('sendmail/',views.sendmail,name='sendmail')
]


