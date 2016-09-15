from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
            max_length=25,
            required=True,
            label="Username",
            widget=forms.TextInput(attrs=
                {'placeholder': 'Username',
                 'name': 'username'}))

    password = forms.CharField(
            max_length=25,
            required=True,
            label='Password',
            widget=forms.PasswordInput(attrs=
                {'placeholder': "Password",
                 'name': 'password'}))
