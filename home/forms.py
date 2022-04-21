from pickle import READONLY_BUFFER
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models

from home.models import Profile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(max_length=20, required=False)
    password2 = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'income', 'expenses', 'balance']
