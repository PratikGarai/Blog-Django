from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class AboutView(TemplateView):
    template_name = 'about.html'


class ArticleListView(ListView):
    template_name = 'BlogApp/article_list.html'
    queryset = models.Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class ArticleDetailView(DetailView):
    template_name = 'BlogApp/article_detail.html'
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return models.Article.objects.filter(published_date__lte=timezone.now())
        return models.Article.objects.all() 


class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_create.html'
    form_class = forms.ArticleForm
    
    def get_queryset(self):
        return models.Article.objects.filter(author=self.request.user)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_update.html'
    form_class = forms.ArticleForm
    
    def get_queryset(self):
        return models.Article.objects.filter(author=self.request.user)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_delete.html'
    
    def get_queryset(self):
        return models.Article.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("BlogApp:Article-List")


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'BlogApp/article_detail.html'

    template_name = 'BlogApp/article_list.html'

    def get_queryset(self):
        return  models.Article.objects.filter(author=self.request.user).filter(published_date__isnull=True).order_by('create_date')


@login_required
def article_publish(request, pk):
    article = get_object_or_404(models.Article, pk=pk)
    post.publish()
    return redirect('BlogApp:Article-Detail', pk=pk)


########   Comments   #########


def add_comment_to_post(request, pk):
    article = get_object_or_404(models.Article, pk=pk)
    if request.method == 'POST':
        form  = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.article = article
            comment.save()
            return redirect('BlogApp:Aritcle-Detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'BlogApp/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.approve()
    return redirect('BlogApp:Article-Detail', pk=comment.article.pk)

@login_required
def comment_remove(request, pk):
    comment =  get_object_or_404(models.Comment, pk=pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('BlogApp:Article-Detail', pk=article_pk)
