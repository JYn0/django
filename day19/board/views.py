from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
# login_required가 있으면 로그인이 요구됨
from django.views.decorators.http import require_GET, require_POST
# require_GET은 get만 받고 다른것은 튕겨냄

# Create your views here.

@login_required
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 유효성 검사
            article = form.save(commit=False) # DB에 쓰지 않겠다
            article.author = request.user     
            article.save() # 진짜 save, commit
            return redirect('board:article_detail',article.id) 
    else: 
        # GET
        form = ArticleForm()
    context = {
        'form': form
    }
    # print(form.errors)
    return render(request, 'board/new_article.html', context)

@ require_GET
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'board/article_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comment_form = CommentForm()
    comments = Comment.objects.all()
    if request.user.is_authenticated:
        is_like = article.like_users.filter(id=request.user.id).exists()
    else:
        islike = None
        
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        'is_like': is_like
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

@login_required
@require_POST
def new_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id) # 사용자가 악의적인 요청을 보냈을때 오류
    form = CommentForm(request.POST) # 데이터 넣고
    if form.is_valid(): # 유효하면
        comment = form.save(commit=False) # 저장하는 척(article_id, author_id가 없어서)
        comment.author = request.user
        comment.article = article
        comment.save()
    return redirect('board:article_detail', article_id)

@require_POST
def toggle_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    if article.like_users.filter(id=user.id).exists():
    # 게시글을 좋아하는 유저중에 요청을 보낸 유저가 있는지
    # DB에서 찾기
    # if user in article.like_user.all(): # python이 찾아서 더 느림
        # 게시글의 좋아요에 좋아하는 user add
        article.like_users.remove(user)
        # user.like_articles(article)
    else: 
        # 좋아하는 목록에서 방금 요청보낸 사용자를 add
        article.like_users.add(user)
    return redirect('board:article_detail', article.id)

    