from django.db import models

class Post(models.Model):
    title = models.TextField()
    body = models.TextField()
    blurb = models.TextField()
    tags = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


