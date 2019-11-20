from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    if request.method == "POST":
        article = Article()
        article.contents = request.POST['contents']
        article.save()
        return redirect('articles')
    else:
        articles = Article.objects.all().order_by("created_at").reverse()
        context = {
            'articles': articles
        }
        return render(request, 'index.html', context)