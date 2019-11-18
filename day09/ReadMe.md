# python
python09

11.18


> **setting**
> Korean Language Pack
> Python
> `pip install pylint`
> `pip install pylint-django`
> 내컴퓨터 - 속성 -설정변경 - 고급 - 환경변수 - PATH - 편집 - 변수 값 복사 - 메모장 붙여넣기 - Ctrl+P - `>settings` - 기본설정:사용자설정열기 - python path - ;변수 값 붙여넣기

### url name space 설정하기
* 각각의 url에 별명을 지어서 html파일에서 사용하는 링크를 추가적으로 바꾸지 않고,
`urls.py`에서만 수정하면 html파일에서도 링크 수정이 반영되게끔 함

```python
# urls.py
app_name = 'articles'

.html
'articles:new'
'articles:create'
```
articles라는 namespace를 만들어주고


### RESTful한 API 설계하기



### Django Admin 설정하기
GET -> 조회
POST -> DB에 반영

|   역할   |   Request-Method   |   End-point   |  Views(Function)    |
| ---- | ---- | ---- | ---- |
|   Create   |   GET   |   /articles/new/   |   new   |
|   Create   |   POST   |   /articles/   |   create   |
|   Read   |   GET   |   /articles/<id>/   |   show   |
|   Read   |   GET   |   /articles/   |   index   |
|   Update   |   GET   |   /articles/<id>/edit/   |   edit   |
|   Update   |   POST   |   /articles/<id>/   |   update   |
|   Delete   |   POST(Delete)   |   /articles/<id>/delete/   |   delete   |



### created_at, updated_at 필드 설정하기
* DateTimeField


```shell
> django-admin startproject crudtest
> cd crudtest
> python manage.py startapp articles
```

```python
# settings.py

INSTALLED_APPS = [
    'articles',
]
LANGUAGE_CODE = 'ko'
TIME_ZONE = 'Asia/Seoul'
USE_TZ = False


# urls.py
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))
    # articles/urls.py안에서 path관리
]


# articles/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index), # ''-> articles
    path('<int:id>/', views.show),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:id>/edit', views.edit),
    path('<int:id>/update', views.update),
    path('<int:id>/delete', views.delete)
]

```

```html
<!-- base.html -->
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
    {% block content %}
    {% endblock %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>

```

`articles` 폴더 안에 `urls.py` 만들기




admin 만들기
```shell
> python manage.py createsuperuser
```