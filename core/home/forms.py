from django import forms




class ContactUsForm(forms.Form):
    email = forms.EmailField(max_length=254)