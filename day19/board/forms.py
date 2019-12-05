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
        exclude = ['date', 'author', 'like_users']
        # html과 검증에서 제외

class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=1, max_length=200)
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['content', ]

