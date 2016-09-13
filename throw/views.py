import json
import random

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from twython import Twython
from throw import streamer

from . import tasks, models, forms

def index(request, template='throw/index.html'):
    try:
        request.session['is_auth']
    except KeyError:
        request.session['is_auth'] = False
    form = forms.TweetForm()
    return render(request, template,
            {'form': form,
             'is_auth': request.session['is_auth']})

def fetch_tweet(request):
    request, tweet_data = tasks.fetch_tweet(request)
    return HttpResponse(
        json.dumps(tweet_data),
        content_type='application/json')

def auth(request):
    t = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SEC)
    auth = t.get_authentication_tokens(callback_url='http://localhost:8000/call_back/')
    request.session['auth_token'] = auth['oauth_token']
    request.session['auth_token_secret'] = auth['oauth_token_secret']
    return redirect(auth['auth_url'])

def callback(request):
    oauth_verifier = request.GET['oauth_verifier']
    twitter = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SEC,
                      request.session['auth_token'], request.session['auth_token_secret'])
    final = twitter.get_authorized_tokens(oauth_verifier)
    request.session['oauth_token'] = final['oauth_token']
    request.session['oauth_token_secret'] = final['oauth_token_secret']
    request.session['is_auth'] = True
    return redirect('/')

def tweet(request):
    if not request.method == 'POST':
        raise Http404('Nah Brah')
    else:
        screen_name = request.POST.get('screen_name', 'error')
        our_message = request.POST.get('tweet_reply_text', '')
        if screen_name == 'error':
            raise Http404('Something Went Wrong')
        t = Twython(settings.APP_KEY, settings.APP_SEC,
                    request.session['oauth_token'], request.session['oauth_token_secret'])
        our_message = '{} {}'.format(our_message, screen_name)
        t.update_status(status=our_message)
        return redirect('/')
