from auti_app.models import Automobil
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class AutomobilForm(forms.ModelForm):
    ime = forms.CharField()
    registracija = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    servis = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Automobil
        fields = '__all__'

class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
