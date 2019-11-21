# python
python12

11.21

### Static File
* **개발환경** vs 배포환경
  * static file : 개발자가 미리 준비해둔 파일
  * 개발환경에서는 app(article)마다 따로 관리
  * 배포환경에서는 정확한 경로를 알려주면 안됨, 한 폴더에서 관리한것처럼 보여야함, 실제 파일의 위치와 보이는 곳이 다름



```html
<!-- index.html -->
{% extends 'base.html' %}

{% load static %} <- 이미지 넣을 준비
{% block stylesheet %}
<style>
.container{
    padding-right: 10rem !important;
    padding-left: 10rem !important;
}
</style>
{% endblock %}
{% block content %}


<img src="{% static '/article/images/car.png' %}" alt="car.png" class="card-img-top" >

<form action="{% url 'articles' %}" method="POST" enctype="multipart/form-data">
<!-- img input tag -->
form에 enctype을 추가해줘야 이미지를 업로드할 수 있다

<!-- base.html -->
    {% block stylesheet %}
    {% endblock %}
```

> pip install Pillow
> python manage.py migrate

```python

# settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
-> media라는 곳에 이미지 관리
MEDIA_URL = '/media/'

# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insta/', include('article.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
-> 이미지가 바로 제공될 수 있도록 url을 만들어 주겠다

```

0(Empty String) vs NULL (vs undefined)


### 이미지 업로드
* 모델 하나에 직접 입력
* 이미지 리사이징
* 이미지 썸네일

```python
# models.py 수정
> pip install django-imagekit

# settings.py
INSTALLED_APPS = [
    'article',
    'imagekit'
]
```


### Multiple 이미지 업로드
* 하나의 Article에 여러 이미지 업로드하기

### JS기본
* 하나의 페이지를 동적으로 만든다
* jQuery -> JS프레임워크(X), JS라이브러리(O)

