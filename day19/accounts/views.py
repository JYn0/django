from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth import logout as auth_logout
# from .forms import AuthenticationForm, UserCreationForm
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def follow(request, user_id):
    fan = request.user # fan : 요청보낸사람
    star = get_object_or_404(id=user_id)
    if fan.stars.filter(id=star.id).exists():
    # fan 입장에서 좋아하는 사람 중에 star.id가 있는지
        fan.stars.remove(star) # unfollow
    else:
        fan.stars.add(star) # follow
    return redirect('accounts:user_detail', star.id)

# url
def signup(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                # 유효성 검사
                user = form.save() # article 객체
                auth_login(request, user)
                # request안에 내용이 있으면 뒤에 무시(로그인상태)
                return redirect('board:article_list') 
        else: 
            # GET
            form = CustomUserCreationForm()

            context = {
                'form': form
            }
            # print(form.errors)
            return render(request, 'accounts/signup.html', context)
    else:
        return redirect('board:article_list')

def login (request):
    if request.user.is_authenticated:
        # 지금 요청을 보낸 사용자가 인증되어있다면(로그인상태)
        return redirect('board:article_list')
    else :
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, request.POST)
            # 인증을 부여해야할때는 param 첫번째는 request
            if form.is_valid():
                # 인증O
                user = form.get_user() # 누구인지 정보 가져오기
                auth_login(request, user) # 로그인상태로 해주기
                return redirect(request.GET.get('next') or 'board:article_list')
                
                # request.GET.get('next') # 없는 index는 return None(null)
                # request.GET['next'] # 없는 index는 error
                # return redirect('board:article_list') 
        else: 
            # GET
            form = CustomAuthenticationForm()
            context = {
                'form': form
            }
            # print(form.errors)
            return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('board:article_list')