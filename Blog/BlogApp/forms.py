from django import forms
from . import models

class ArticleForm(forms.ModelForm):
    
    class Meta():
        model = models.Article
        fields = '__all__'
