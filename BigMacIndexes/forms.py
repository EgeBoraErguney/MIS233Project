from django import forms
from .country_choices import COUNTRY_CHOICES


class CountryGraphForm(forms.Form):
    country1 = forms.CharField(label='Country1', widget=forms.Select(choices=COUNTRY_CHOICES))
    country2 = forms.CharField(label='Country2', widget=forms.Select(choices=COUNTRY_CHOICES))


class ContactUsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name", }))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control", "type": "email", "placeholder": "E-mail address", }))
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Text", "size": 20}))

