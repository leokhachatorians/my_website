from django.contrib import messages
from django.contrib.auth import (
        authenticate, login as login_user,
        logout as logout_user)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from . import forms, models

def index(request, template='me/index.html'):
    return render(request, template)

def about(request, template='me/about.html'):
    return render(request, template)

def resume(request, template='me/resume.html'):
    return render(request, template)

def projects(request, template='me/projects.html'):
    return render(request, template)

def login(request, failed_template='me/login.html', successful_template='me/index.html'):
    login_form = forms.LoginForm()
    if request.user.is_authenticated():
        messages.info(request, 'Already Logged In Brah',
                extra_tags='login_message')
        return redirect('/')

    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                messages.info(request, 'Logged In',
                        extra_tags='login_message')
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials',
                        extra_tags='wrong_login')
                return render(request, failed_template,
                        {'login_form': login_form})
    return render(request, failed_template,
            {'login_form': login_form})

def logout(request, template='me/login.html'):
    if request.user.is_authenticated():
        logout_user(request)
        messages.info(request, "Logged Out", extra_tags='login_message')
    return redirect('/')

def blog(request, template='me/blog.html'):
    queryset = models.Post.all().order_by('-id')
    paginator = Paginator(queryset, 10)
