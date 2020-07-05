from django import forms
from . import models

class ArticleForm(forms.ModelForm):
    
    class Meta():
        model = models.Article
        fields = ('author','title','text')

        widgets = {
                'title' : forms.TextInput(attrs ={'class' : 'textinputclass'}),
                'text' : forms.Textarea(attrs = {'class' : 'editable medium-editor-textarea postcontent'})
                }


class CommentForm(forms.ModelForm):

    class Meta():
        model = models.Comment
        fields = ('author','text')

        widgets = {
                'author' : forms.TextInput(attrs = {'class' : 'textinputclass'}),
                'text' : forms.Textarea(attrs = {'class' : 'editable medium-editor-textarea'})
                }
