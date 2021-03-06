# python
python19

12.02



### 프로젝트 환경관리

* **독립환경 구축**

  * 프로젝트 안에 설치 -> 외부에서 접근 불가, 외부 것으로 접근하지 않기
  * 독립된 환경 -> 가상환경
  



```shell
~/Desktop/django/day19

$ tocch .gitignore

독립된 workspace 만들기
$ python -m venv venv
$ source venv/Scripts/activate
(venv)
이 시점부터 터미널이 독립된 공간(venv)을 본다(venv가 없으면 글로벌)
$ pip list
pip
setuptools
python 초기 상태
$ pip install django # + other packages
$ python -m pip install --upgrade pip

$ source venv/Scripts/activate대신 python install 상태에서
F1 -> >select interpreter -> .\venv\... 선택하면 시작할때 윗줄을 자동으로 실행해줌

# $ pip freeze
# 설치해놓은 패키지들의 버전까지 확인하여 얼리겠다
# $ touch requirements.txt
# freeze해놓은 것 적어두기
$ pip freeze > requirements.txt
```

```shell
# 중요(정리)

$ python -m venv venv
F1 -> >select interpreter -> .\venv\... 
$ touch .gitignore
$ pip install django # + other packages
$ pip freeze > requirements.txt
```



```gitignore
# .gitignore
venv/
다운로드 되어있어서 용량이 클 venv폴더는 무시한다
.vscode/

무시해야할 코드들 gitignore.io에서 생성해서 복붙, 
.vscode/는 따로 써줘야함

db.sqlite3 -> 데이터베이스는 공유하면 안되지만, sync 맞출때는 알아서...

올라간 파일 ignore로 지우기
$ git rm -r --cached 폴더
$ git rm --cached 파일
```

extensions : django(0.19.0) install

Ctrl + , -> Associations -> edit in settings.json - extension:Django의 usage 복붙



-----------------------



```shell
$ django-admin startproject django_advance .
-> depth의 차이
$ python manage.py startapp board
$ touch board/urls.py
```

```python
# settings.py
INSTALLED_APPS = [
    'board',
]
# Ctrl + g -> 몇번째 줄인지 찾을 수 있음



# urls.py
# board/urls.py
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name="article_list"),
]



# views.py
from django.shortcuts import render

# Create your views here.
def article_list(request):
    return render(request, 'board/article_list.html')



# models.py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    keyword = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

```shell
$ python manage.py makemigrations
$ python manage.py migrate board
$ pip install faker
```



```python
# models.py
from faker import Faker
f = Faker()

@classmethod
    def dummy(cls, n):
        # article = cls()
        # article.title = '~~'
        # article.content = 
        # ...
        # article.save()

        # cls : 자신, 위의 내용을 줄인 것
        for i in range(n):
            cls.objcets.create(
                title= f.text(20),
                contetn= f.text(),
                keyword= f.company(),
                email= f.email(),
            )
```

```shell
$ python manage.py shell
>>> from board.models import Article
>>> Article.dummy(20)
$ pip install django_extensions
settings.py에서 INSTALLED_APPS = ['django_extensions',] 추가

$ pip install ipython

$ python manage.py shell_plus
In [1]: Article.dummy(20)

extensions -> install SQLite, vscode-icons(9.6.0)
db.sqlite3 오른쪽버튼 opendata
SQLITE EXPLORER play버튼 누르면 데이터에 들어간 내용 볼 수 있음
```


```python
# views.py
from django.shortcuts import get_object_or_404
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

```


`pip freeze > requirements.txt`하고 끝내기

---------------

# 12.03
> pip install django-bootstrap4

```python
# settings.py

INSTALLED_APPS = [
    'bootstrap4'
]
```


---------------

# 12.04

### accounts

```shell
> python manage.py createsuperuser

```

`settings.py`에  `AUTH_USER_MODEL = 'accounts.User'`
-> 기본 user모델이 아닌 내가 만든 user모델을 사용하겠다



`accounts/views.py`
```python
from .forms import CustomAuthenticationForm, CustomUserCreationForm
# -> 내가 만든 user 모델

def signup(request):
    if 요청을 보낸 사용자가 인증되어있지 않으면:
        if method가 POST이면:
            if 유효성 검사를 통과한다면:
                user db에 저장하고
                저장 정보로 login해주고
                return 게시판 목록으로 이동
        else:
            GET이면
            그냥 signup페이지 접속해오면
            context 정보 담아서
            return signup페이지로 이동
    else:
        인증되어있다면
        return 게시판 목록으로 이동

def login(request):
    if 요청을 보낸 사용자가 인증되어있으면(로그인상태):
        return 게시판 목록으로 이동
    else:
        로그아웃 상태
        if POST 방식이면:
            로그인할때 보낸것들을 form에 담아두기
            if form이 유효해서:
                인증이 되었으면
                누구 정보인지 가져와서
                로그인을 해주고
                return 로그인페이지 오기 전 이나, 목록으로 이동
        else :
            GET방식이면(로그인하러 들어온 페이지)
            기본틀을 context에 담아서
            login페이지로 넘겨주면
            return 틀대로 로그인페이지가 꾸려진다.

def logout(request):
    로그아웃하고
    return 게시판 목록으로 이동

```

`board/views.py`
```python
from django.contrib.auth.decorators import login_required
# login_required가 있으면 로그인이 요구됨

@login_required
# 로그인이 되어있어야 새 게시글을 작성할 수 있음
def new_article(request):

```

`accounts/forms.py`
```python
class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(min_length=3)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('address', ) # 원래 있던 field에 address도 추가

class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User

```
`accounts/models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 여러 정보 담기
    address = models.CharField(max_length=200)
```

---------------

# 12.05

### comment + like + follow

* board/views.py
* article_detail.html


GET -> R

POST -> CUD, DB에 영향이 갈 때


```shell
> python manage.py shell_plus --print-sql
```

---------------

```shell
# master 안 떠있을 경우
$ git init
$ git add .
$ git commit -m ""
$ git push origin master
```
