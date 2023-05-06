from django import forms
from .models import Job



class SaveJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude=['company','job_keys']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','placeholder':"نام شرکت خود را وارد کنید"}),
            'email' : forms.TextInput(attrs={'class': 'form-control','placeholder':"info@gmail.com"}),
            'salary':forms.TextInput(attrs={'class': 'form-control','placeholder':"حقوق از"}),
            'info': forms.Textarea(attrs={'class': 'form-control',}),
            'necessary': forms.Textarea(attrs={'class': 'form-control',}),
            'ostan':forms.Select(attrs={'class': 'form-control',}),
            'privilege':forms.Textarea(attrs={'class': 'form-control',}),
            'category':forms.Select(attrs={'class': 'form-control','placeholder':"تهران"}),
        }