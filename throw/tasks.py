from __future__ import absolute_import
import random
from celery import task
from celery.task import periodic_task
from celery.schedules import crontab
from django.conf import settings
from .streamer import Streamer
from throw import models

@task
def refresh():
    models.Tweets.objects.all().delete()
    stream = Streamer(
        settings.TWITTER_APP_KEY,
        settings.TWITTER_APP_SEC,
        settings.TWITTER_TOKEN,
        settings.TWITTER_TOKEN_SEC
    )
    while not stream.done:
        stream.statuses.filter(track=settings.TRACK)

@task
def fetch_tweet(request):
    try:
        request.session['viewed']
    except KeyError:
        request.session['viewed'] = []
    if len(request.session['viewed']) > 80:
        request.session['viewed'] = []

    random_index = random.randint(0, 99)
    request.session['viewed'].append(random_index)

    try:
        tweet = models.Tweets.objects.all()[random_index]
        links = search_for_links(tweet.tweet)
        tweet_pos = get_position()
        tweet_data = {
            'name': tweet.name,
            'screen_name': tweet.screen_name,
            'tweet': tweet.tweet,
            'location': tweet.location,
            'profile_pic': tweet.profile_pic,
            'larger_pic': tweet.profile_pic.replace('_normal', '_400x400'),
            'links': links,
            'mentions': tweet.mentions,
            'css_top': tweet_pos[0],
            'css_left': tweet_pos[1],
        }

        return request, tweet_data
    except IndexError:
        return request, None

def get_position():
    return (
            random.randint(10, 80),
            random.randint(2, 78)
    )

def search_for_links(tweet):
    links = {
        'found':[]
    }

    indexes = list(find_all(tweet, 'https://t.co/'))
    if not indexes:
        return links

    for i in indexes:
        links['found'].append(
            tweet[i:i+23]
        )
    return links

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)
