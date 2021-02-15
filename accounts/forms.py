from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput

class UserLoginForm(forms.ModelForm):
    username = CharField()
    password = CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
