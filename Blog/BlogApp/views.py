from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms

class ArticleListView(ListView):
    template_name = 'BlogApp/article_list.html'
    queryset = models.Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'BlogApp/article_detail.html'
    queryset = models.Article.objects.all() 
 
class ArticleCreateView(CreateView):
    template_name = 'BlogApp/article_create.html'
    queryset = models.Article.objects.all() 
    form_class = forms.ArticleForm

class ArticleUpdateView(UpdateView):
    template_name = 'BlogApp/article_update.html'
    queryset = models.Article.objects.all() 
    form_class = forms.ArticleForm

class ArticleDeleteView(DeleteView):
    template_name = 'BlogApp/article_delete.html'
    queryset = models.Article.objects.all()   

    def get_success_url(self):
        return reverse("BlogApp:Article-List")
