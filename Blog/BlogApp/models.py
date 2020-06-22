from django.db import models
from django.urls import reverse

class Article(models.Model):

    title = models.CharField(max_length = 500)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("BlogApp:Article-Detail", kwargs = {'pk': self.pk })
