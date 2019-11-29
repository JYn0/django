# python
python18

11.29

### Pusher
-> 채팅, 실시간 댓글/좋아요 반영 기능

ajax는 요청을하고 페이지 refresh없이 데이터를 받아서 바꾸는 형식

pusher는 ajax로 요청하는 것은 맞지만, success 하지 않고 JS에 코드가 들어감


> https://pusher.com/
> Channels Billing
> * Max Concurent Connetions : 최대 동시 접속자 가능 수
> * MEssages / Day : 한번에 페이지 상태를 보낼수 있는 수


**페이지 단위로 채널 관리**

```shell
> django-admin startproject chatproject
> cd chatprojcet
> python manage.py startapp boards

> pip install pusher
```

```python
# settings.py
INSTALLED_APPS = [
    'boards',
    'accounts',
]
LANGUAGE_CODE = 'ko'
TIME_ZONE = 'Asia/Seoul'
USE_TZ = False


# chatproject/chatproject/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls'))
]


# chatproject/boards/urls.py
from django.urls import path
from . import views
app_name = "boards"
urlpatterns = [
    path('', views.index, name="index"), # main 페이지는 채팅 목록
    path('<int:room_id>/', views.show, name="room"), # 채팅방
]

# chatproject/boards/views.py

# chatprojcet/boards/templates/index.html
# chatprojcet/boards/templates/show.html
```
