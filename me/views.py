from django.shortcuts import render

def index(request, template='me/index.html'):
    return render(request, template)

def index2(request, template='me/index2.html'):
    return render(request, template)

def about(request, template='me/about.html'):
    return render(request, template)

def resume(request, template='me/resume.html'):
    return render(request, template)

def projects(request, template='me/projects.html'):
    return render(request, template)

