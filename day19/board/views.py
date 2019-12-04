from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# login_required가 있으면 로그인이 요구됨

# Create your views here.

@login_required
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 유효성 검사
            article = form.save() # article 객체
            return redirect('board:article_detail',article.id) 
    else: 
        # GET
        form = ArticleForm()
    context = {
        'form': form
    }
    # print(form.errors)
    return render(request, 'board/new_article.html', context)

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'board/article_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article
    }
    return render(request, 'board/article_detail.html', context)

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article,id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # article을 request.POST로 받아온 데이터로 무언가를 할 것이다.
        if form.is_valid():
            article = form.save() # article 객체
            return redirect('board/new_article.html') 
    else: 
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'board/article_form.html', context)
