# python
python08

11.15

> crudtest/crudtest/ `settings.py` `urls.py`
> crudtest/boards/ `views.py`
> crudtest/boards/templates/ `index.html` `new.html` `show.html`

### review
* Naver Api 사용해보기
  * 외부 사이트에 Request를 보낼 때, Post방식으로 요청하는 방법
  * Request Body에 JSON형식으로 파라미터를 보내는 방법
* ORM 기초
  * Create, Read를 Django Shell에서 실행
  * ORM(Object Relationship Mapping)이 무엇인지, 왜 사용하는지?


### 기본 게시판 만들기
* URL 분리하기
  * `urls.py`에 우리가 접속할 모든 주소 명시한 것을 CRUD를 하다보면 만들어야 할 페이지가 점점 많아서 구분하기가 어려워지기 때문에 각 역할을 하는 App마다 `urls.py`파일을 생성할 예정
    > C - New(입력), Create(실제로 DB에 반영)
    > R - Index(전체 List), Show(한개)
    > U - Edit(수정), Update(실제로 DB에 반영)
    > D - Delete

* 공용(공유)으로 사용할 수 있는 HTML파일 만들기
  * 반복되는 HTML 구조를 계속해서 새로 만들지 말고 공통되는 부분은 하나의 파일로 묶어서 반복해서 사용


* CRUD

```shell
> django-admin startproject crudtest
> cd .\crudtest
> python manage.py startapp boards
> python manage.py runserver
```


`settings.py` `urls.py`
```python
# crudtest/settings.py
INSTALLED_APPS = [
    'boards'
]
LANGUAGE_CODE = 'ko'
TIME_ZONE = 'Aisa/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# crudtest/urls.py
from boards import views as boards_views
urlpatterns = [
    path('admin/', admin.site.urls),
    # 게시판의 메인페이지, 전체 리스트 페이지
    path('boards/', boards_views.index),
    # 게시판의 새 글을 작성하는 페이지
    path('boards/new/', boards_views.new),
    # 게시판의 글 하나를 상세히 보는 페이지
    path('boards/<id>/', boards_views.show)
]
```


```shell
> python manage.py makemigrations 
# makemigrations-> DB에 table을 만들어주기위한 migration을 만들어주는 것, 001_initial.py생김
# 환경을 만들 수 있는 파일을 만드는 것(구조 파일 만드는 것)
> python manage.py migrate 
# migrate -> 동작시키는거


```


https://getbootstrap.com/
get start
CSS(head에), JS(body 끝나기 전에) 복사

templates/base.html -> 기본이 되는 html 파일
{% block content %}
이 부분에 들어갈 내용만 작성하면 됨
{% endblock %} 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
        <h5 class="my-0 mr-md-auto font-weight-normal">^_^</h5>
        <nav class="my-2 my-md-0 mr-md-3">
            <a class="p-2 text-dark" href="/boards">홈</a>
            <a class="p-2 text-dark" href="/boards">게시판</a>
        </nav>
        <a class="btn btn-outline-primary" href="#">Sign up</a>
    </div>    
    <div class="container">
        {% block content %}
        {% endblock %}        
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```


`views.py`
```python
# day08/crudtest/boards/views.py


```
