from django.shortcuts import render, redirect

from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        creator = request.POST['creator']

        article = Article()
        article.title = title
        article.contents = contents
        article.creator = creator
        article.save()       
        return redirect('articles:show', article.id)

    return render(request, 'new.html')


def show(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    return render(request, 'show.html', context)

'''
def create(request):
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']

    article = Article()
    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()
    # show로 넘어가기
    return redirect('articles:show', article.id)
'''
def edit(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)

        article.title = request.POST['title']
        article.contents = request.POST['contents']
        article.creator = request.POST['creator']
        article.save()
        return redirect('articles:show', article.id)
    else :
        article = Article.objects.get(id=id)
        context = {
            'article': article
        }
        return render(request, 'edit.html', context)
'''
def update(request, id):
    article = Article.objects.get(id=id)

    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']

    article.title = title
    article.contents = contents
    article.creator = creator
    article.save()
    return redirect('articles:show', article.id)
'''
def delete(request, id):
    # if request.method == "POST":
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')
