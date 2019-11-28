from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Article, Comment, ArticleImages, Board, HashTag
import json

# Create your views here.

def js_test(request):
    return render(request, 'js_test.html')
def jq_test(request):
    boards = Board.objects.all().order_by('created_at').reverse()
    context = {
        'boards': boards
    }
    return render(request, 'jq_test.html', context)

def submit_boards(request):
    if request.method == "POST":
        contents = request.POST["board"]
        board = Board.objects.create(contents=contents) # 컬럼이 contents
        context = {
            'board': board
        }
        return render(request, 'empty.html', context)

def delete_boards(request):
    if request.method == "POST":
        id = request.POST["board_id"]
        board = Board.objects.get(id=id)
        board.delete()
        context = {
            'board_id': id
        }
        # HttpResponse(보낼data, json타입 알려주기), html파일을 따로 만들 필요 없음
        return HttpResponse(json.dumps(context), content_type="application/json")
    
def edit_boards(request):
    if request.method == "POST":
        id = request.POST["board_id"]
        contents = request.POST["contents"]
        board = Board.objects.get(id=id)
        board.contents = contents
        board.save()
        return HttpResponse('', status=204)

def index(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            article = Article()
            article.contents = request.POST['contents']
            article.user_id = request.user.id  
            article.save() 

            tags = request.POST["hashtag"]
            for tag in tags.split(","):
                tag = tag.strip() # 앞,뒤의 공백 삭제
                if not HashTag.objects.filter(tag=tag):
                    tag = HashTag.objects.create(tag=tag)
                else:
                    tag = HashTag.objects.filter(tag=tag)[0]
                article.tags.add(tag)


            # 이미지는 무조건 POST로만 
            # input type의 name과 같아야함
            # 원본 이미지 저장
            # article.image = request.FILES["image"] 
            # 원본 이미지를 프로세싱 한 이미지 저장
            # article.image_resized = request.FILES["image"]

            article.save()
            for image in request.FILES.getlist("image"):
                ArticleImages.objects.create(article_id=article.id, image=image)
            return redirect('articles')
        else:
            return redirect('accounts:login')
    else:
        articles = Article.objects.all().order_by("created_at").reverse()
        context = {
            'articles': articles
        }
        return render(request, 'index.html', context)

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.is_permitted(request.user.id):
        if request.method == "POST":
            article.contents = request.POST["contents"]
            article.save()
            return redirect('articles')
        else: 
            context = {
                'article': article
            }
        return render(request, 'article/edit.html', context)
    else:
        return redirect('articles')

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.is_permitted(request.user.id):
        article.delete()
        return redirect('articles')
    else:
        return redirect('articles')    

def comments(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            contents = request.POST['contents']
            article_id = request.POST['article_id']

            if request.POST["form_method"] == "create":
                comment = Comment()
            elif request.POST["form_method"] == "edit":
                comment_id = request.POST["comment_id"]
                comment = Comment.objects.get(id=comment_id)
                if comment.user_id != request.user.id:
                    return HttpResponse('', status=401)

            # if comment.user_id != request.user.id:
            #     return HttpResponse('', status=401)
            # else: 
            comment.contents = contents
            comment.article_id = article_id
            comment.user_id = request.user.id
            comment.save()
            context = {
                'method': request.POST["form_method"],
                'comment': comment.contents,
                'username': comment.user.username,
                'comment_id': comment.id,
                'article_id': comment.article_id
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        else:
            context = {
                'status': 401,
                'message': '로그인이 필요합니다'
            }
            return HttpResponse(json.dumps(context), status=401, content_type="application/json")


def delete_comment(request):
    if request.method == "POST":
        comment_id = request.POST["comment_id"]
        comment = Comment.objects.get(id=comment_id)
        if comment.user_id == request.user.id:
            comment.delete()
            return HttpResponse('', status=204)
        else:
            return HttpResponse('', status=401)

            

def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        comment.contents = request.POST["contents"]
        comment.save()
        return redirect('articles')
    else: 
        context = {
            'comment': comment
        }
        return render(request, 'comment/edit.html', context)

def likes(request):
    if request.method == "POST" and request.user.is_authenticated:
        article_id = request.POST["article_id"]
        article = Article.objects.get(id=article_id)
        if request.user in article.user_likes.all():
            article.user_likes.remove(request.user) # 좋아요 취소
        else:
            article.user_likes.add(request.user) # 좋아요
            
        likes_count = len(article.user_likes.all())
        context = {
            'count': likes_count
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
    else: 
        return HttpResponse('', status=403)