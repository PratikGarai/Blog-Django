from django.db import models
from django.urls import reverse
from django.utils import timezone

class Article(models.Model):
    
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def get_absolute_url(self):
        return reverse("BlogApp:Article-Detail", kwargs = {'pk': self.pk })

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length = 50)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse("BlogApp:Article-List")   

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
