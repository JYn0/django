from django import forms
# from django.db import models
from .models import Article, Comment

# django forms validation
class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, strip=True)
    email = forms.EmailField()
    class Meta:
        model = Article
        # fields = '__all__'
        # fields = ('title', 'content')
        exclude = ['date']