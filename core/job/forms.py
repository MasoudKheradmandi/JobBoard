from django import forms
from .models import Job



class SaveJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','placeholder':"نام شرکت خود را وارد کنید"}),
            'email' : forms.TextInput(attrs={'class': 'form-control','placeholder':"info@gmail.com"}),
            'salary':forms.TextInput(attrs={'class': 'form-control','placeholder':"حقوق از"}),
            'job_keys' : forms.TextInput(attrs={'class': 'form-control tags_input',}),
            'info': forms.Textarea(attrs={'class': 'form-control',}),
            'necessary': forms.Textarea(attrs={'class': 'form-control',}),
            'ostan':forms.TextInput(attrs={'class': 'form-control','placeholder':"تهران"}),
            'privilege':forms.Textarea(attrs={'class': 'form-control',}),
        }