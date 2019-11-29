from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # user라는 변수에 값을 넣고 저장
            user = form.save() # 회원가입 끝
            auth_login(request, user) # login
            return redirect('boards:index')
        else:
            return render(request, 'signup.html')
    else:
        # request.method == "GET":
        # login상태에서 들어올때
        if request.user.is_authenticated:
            return redirect('boards:index')
        else :
            return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
        else:
            return render(request, 'login.html')
    else:
        # login상태에서 들어올때
        if request.user.is_authenticated:
            return redirect('boards:index')
        else :
            return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('boards:index')
