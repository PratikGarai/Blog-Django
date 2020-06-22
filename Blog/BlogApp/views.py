from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models

class ArticleListView(ListView):
    queryset = models.Article.objects.all()
