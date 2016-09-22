from django.contrib import messages
from django.contrib.auth import (
        authenticate, login as login_user,
        logout as logout_user)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def logout(request, template='me/login.html'):
    if request.user.is_authenticated():
        logout_user(request)
        messages.info(request, "Logged Out", extra_tags='login_message')
    return redirect('/')

def blog(request, template='me/blog_nav.html'):
    queryset = models.Post.objects.all().order_by('-id')
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, template, {'posts':posts})

def blog_post(request, template='me/blog_post.html', num='1'):
    post = get_object_or_404(models.Post, pk=num)
    return render(request, template, {'post':post})

@login_required
def new_post(request, template='me/new_post.html'):
    new_post_form = forms.NewPostForm()
    if request.method == 'POST':
        new_post_form = forms.NewPostForm(request.POST)
        if new_post_form.is_valid():
            title = new_post_form.cleaned_data['title']
            body = new_post_form.cleaned_data['body']
            blurb = new_post_form.cleaned_data['blurb']
            tags = new_post_form.cleaned_data['tags']
            models.Post.objects.create(
                    title=title, body=body,
                    blurb=blurb, tags=tags,
                    )
            return redirect('/blog')
    return render(request, template,
            {'new_post_form': new_post_form})
