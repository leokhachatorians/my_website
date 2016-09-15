from django.db import models

class Post(models.Model):
    title = models.TextField()
    body = models.TextField()
    tags = models.TextField()
    date_posted = models.DateTimeField()
