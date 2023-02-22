from django import forms
from .models.company import Company
from django.contrib.auth import get_user_model


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


