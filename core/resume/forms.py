from django import forms 
from .models import SendResume

class FormSender(forms.ModelForm):
    class Meta:
        model = SendResume
        fields = ['cv_file',]