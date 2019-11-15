from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

# 게시글 제목, 내용, 작성자

def index(request):
    # Board 모델에 담긴 모든 글들을 가져와서 보여줌
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'index.html', context)

def new(request):

    return render(request, 'new.html')


def create(request):
    # new서 작성한 내용을 받아서 사용
    title = request.GET['title']
    contents = request.GET['contents']
    creator = request.GET['creator']

    # 방법1
    # new_board = Board()
    # new_board.title = title
    # new_board.contents = contents
    # new_board.creator = creator
    # new_board.save()
    # 방법2
    # new_board = Board(title=title, contents=contents, creator=creator)
    # new_board.save()
    # 방법3(위 두줄을 하나로 만드는 방법)
    new_board = Board.objects.create(title=title, contents=contents, creator=creator)

    return redirect(f'/boards/{new_board.id}')
    

def show(request, id):
    board = Board.objects.get(id=id)
    # (id=int(id))
    context = {
        'board': board
    }
    return render(request, 'show.html', context)

def edit(request, id):
    # 원래 있던 내용이 들어있는 Form
    board = Board.objects.get(id=id)
    context = {
        'board': board
    }
    return render(request, 'edit.html', context)
    
def update(request, id):
    # 실제로 update가 일어나는 곳
    board = Board.objects.get(id=id)
    title = request.GET['title']
    contents = request.GET['contents']

    board.title = title
    board.contents = contents
    board.save()

    context = {
        'board': board
    }
    # render 직접 뿌리기
    # redirect : 다른곳으로 연결
    return redirect(f'/boards/{board.id}')

def delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect(f'/boards')