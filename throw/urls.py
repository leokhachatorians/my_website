from django.conf.urls import url
from throw import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'fetch$', views.fetch_tweet),
    #url(r'^auth/', views.auth),
    #url(r'^call_back/', views.callback),
    url(r'tweet$', views.tweet, name='tweet'),
]
