from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        '''
        The job of this function is,
        to change the field we want
        '''
        user = super().save(commit=False)
        user.is_active = False # This field becomes to False
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']