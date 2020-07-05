from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(TemplateView):
    template_name = 'about.html'


class ArticleListView(ListView):
    template_name = 'BlogApp/article_list.html'
    queryset = models.Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class ArticleDetailView(DetailView):
    template_name = 'BlogApp/article_detail.html'
    queryset = models.Article.objects.all() 
 

class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_create.html'
    queryset = models.Article.objects.all() 
    form_class = forms.ArticleForm


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_update.html'
    queryset = models.Article.objects.all() 
    form_class = forms.ArticleForm


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_delete.html'
    queryset = models.Article.objects.all()   

    def get_success_url(self):
        return reverse_lazy("BlogApp:Article-List")


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_list.html'
    queryset = models.Article.objects.filter(published_date__isnull=True).order_by('create_date')
