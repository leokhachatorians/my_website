from django.shortcuts import render

def index(request, template='me/index.html'):
    return render(request, template)
