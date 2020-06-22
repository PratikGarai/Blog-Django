from django.db import models

class Article(models.Model):

    title = models.CharField(max_length = 500)
    content = models.TextField()
