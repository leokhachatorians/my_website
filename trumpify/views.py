import json

from django.http import HttpResponse
from django.shortcuts import render
from .trumper import trumpify

def index(request, template='trumpify/index.html'):
    return render(request, template)

def fetch(request):
    tweet = trumpify(request)
    return HttpResponse(
        json.dumps(tweet),
        content_type='application/json')
