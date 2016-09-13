from django.db import models

class Tweets(models.Model):
    name = models.TextField()
    screen_name = models.TextField()
    tweet = models.TextField()
    location = models.TextField(null=True)
    profile_pic = models.TextField()
    mentions = models.TextField()
