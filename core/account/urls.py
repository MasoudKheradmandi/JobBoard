from django.urls import path
from . import views

app_name = "account"


urlpatterns = [
    path('company_register/',views.company_signup,name='signup_company'),
    path('company_profile/',views.CompanyProfile,name='company_profile'),
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.user_signup,name='user_signup'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('reset_token/',views.reset_token,name='reset_token'),
    path('verify/',views.verify,name='verify'),
    path('changepassword/',views.new_password,name='new_password'),
    path('suggest/',views.suggest_job_for_user,name='suggest_job_for_user'),
]


