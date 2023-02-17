from django.urls import path
from . import views


urlpatterns = [
    path('company_register/',views.SignUp,name='signup_company'),
]


