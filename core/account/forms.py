from django import forms
from .models.company import Company
from django.contrib.auth import get_user_model
from .models.user_profile import UserProfile

User = get_user_model()


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        # fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','placeholder':"نام شرکت خود را وارد کنید"}),
            'email' : forms.TextInput(attrs={'class': 'form-control','placeholder':"info@gmail.com"}),
            'website':forms.URLInput(attrs={'class': 'form-control','placeholder':"نام وبسایت"}),
            'date_foundations' : forms.TextInput(attrs={'class': 'form-control','placeholder':"17/12/1400"}),
            'locations' : forms.Textarea(attrs={'class': 'form-control',}),
            'info': forms.Textarea(attrs={'class': 'form-control',}),
            'phone':forms.TextInput(attrs={'class': 'form-control','placeholder':"234734858"}),
            'ostan':forms.TextInput(attrs={'class': 'form-control','placeholder':"تهران"}),
            'city':forms.TextInput(attrs={'class': 'form-control','placeholder':"بابلسر"}),
            'code_posty':forms.TextInput(attrs={'class': 'form-control','placeholder':"4741688093"}),
            'instagram':forms.URLInput(attrs={'class': 'form-control',}),
            'linkedin':forms.URLInput(attrs={'class': 'form-control','placeholder':"https://www.linkedin.com/"}),
            'telegram':forms.URLInput(attrs={'class': 'form-control'}),
            'facebook':forms.URLInput(attrs={'class': 'form-control','placeholder':"https://www.facebook.com/"}),

        }
        exclude = ['user',]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user',]

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','placeholder':"نام خود را وارد کنید"}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control','placeholder':"نام خانوادگی"}),
            'job':forms.URLInput(attrs={'class': 'form-control','placeholder':"تخصص خود را وارد بنویسید"}),
            'age' : forms.TextInput(attrs={'class': 'form-control','placeholder':"21"}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control','placeholder':"234734858"}),
            'city':forms.TextInput(attrs={'class': 'form-control','placeholder':"بابلسر"}),
            'code_posty':forms.TextInput(attrs={'class': 'form-control','placeholder':"4741688093"}),
            'address' : forms.Textarea(attrs={'class': 'form-control','placeholder':"این قسمت بصورت private است و نمایش داده نمیشود"}),
            'info': forms.Textarea(attrs={'class': 'form-control','placeholder':"در مورد خود بیشتر توضیح دهید"}),
            'tahsilat':forms.TextInput(attrs={'class': 'form-control','placeholder':"دیپلم"}),
            'linkedin':forms.URLInput(attrs={'class': 'form-control','placeholder':"https://www.linkedin.com/"}),
        }
