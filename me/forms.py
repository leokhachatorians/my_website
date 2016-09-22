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

class NewPostForm(forms.Form):
    title = forms.CharField(
            max_length=200,
            required=True,
            label="Title",
            widget=forms.TextInput(attrs=
                {'placeholder': 'Title',
                 'name': 'title'}))

    blurb = forms.CharField(
            required=True,
            label="Blurb",
            widget=forms.Textarea(attrs=
                {'placeholder': 'Blurb',
                 'rows': 4,
                 'cols': 55,}))

    body = forms.CharField(
            required=True,
            label="Body",
            widget=forms.Textarea(attrs=
                {'placeholder': 'Body',
                 'rows': 4,
                 'cols': 55,}))

    tags = forms.CharField(
            max_length=150,
            label='Tags',
            widget=forms.TextInput(attrs=
                {'placeholder': 'Tags',
                 'name': 'tags'}))
