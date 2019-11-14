# python
python07

11.14

> day07/naverapi/

### 네이버 API 사용

https://developers.naver.com/main/
Products - 서비스API - 데이터랩 - 오픈API이용신청 
사용API :  데이터랩(검색어트렌드)
웹서비스 : http://localhost:8000
Products - 서비스API - 데이터랩 - 개발가이드보기
(https://developers.naver.com/docs/datalab/search/)

```
> cd day07
> django-admin startproject naverapi
> cd naverapi
> python manage.py startapp search_trend
> python manage.py runserver
```

```python
# day07/naverapi/settings.py
INSTALLED_APPS = [
    'search_trend' # application 등록
]
LANGUAGE_CODE = 'ko'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True # I, N사이에 18글자가 있다, internationalization, 개발자가 지역화 지원을 위해 소프트웨어적으로 준비하는 것(정해져있는 문구 바로 대치)
USE_L10N = True # L, N사이에 18글자가 있다, localization, 번역가가 번역하고 지역 형식에 맞게 변환하는 것
USE_TZ = False # use timezone, true이면 default값이 들어감


# day07/naverapi/urls.py
from search_trend import views as search_trend_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # 검색어를 입력하는 곳
    path('search/', search_trend_view.search),
    # 검색어에 대한 트렌드 결과를 받는 곳
    path('search/result', search_trend_view.result)
]


# day07/search_trend/views.py
from django.shortcuts import render
import json
import requests

# Create your views here.
def search(request):
    # 검색어를 입력하는 곳
    return render(request,'search.html')

def result(request):
    # 검색어에 대한 검색 트렌드를 받아보는 곳
    start_date = request.GET['search_start_date']
    end_date = request.GET['search_end_date']
    time_unit = request.GET['search_time_unit']
    group_name = request.GET['search_group_name']
    keywords = request.GET['search_keywords'].split(',')

    query = {
        "startDate": start_date,
        "endDate": end_date,
        "timeUnit": time_unit,
        "keywordGroups": [
          {
            "groupName": group_name,
            "keywords": keywords
          }
        ]
    }

    
    url = 'https://openapi.naver.com/v1/datalab/search'
    client_id = 'key'
    client_secret = 'secret'

    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    params = json.dumps(query) # dictionary to JSON

    response = requests.post(url, headers=headers, data=params)
    # POST방식은 url, headers, data를 보내야함
    result = response.text

    context = {
        'result': result
        # 'result': {
        #     'start_date': start_date,
        #     'end_date': end_date,
        #     'time_unit': time_unit,
        #     'group_name': group_name,
        #     'keywords': keywords
        # }
    }

    return render(request,'result.html', context)
```

```html
<!-- day07/naverapi/search_trend/templates/search.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>검색어를 입력하세요.</h1>
    <form action="/search/result">
        <!-- <input type="text" name="search_keyword"> -->
        <label>기간 시작날짜</label>
        <input type="date" name="search_start_date">
        <br/>
        <label>기간 종료날짜</label>
        <input type="date" name="search_end_date">
        <br/>
        <label>구간 단위</label>
        <select name="search_time_unit">
            <option value="date">일간</option>
            <option value="week">주간</option>
            <option value="month">월간</option>
        </select>
        <br/>
        <label>검색어 그룹명</label>
        <input type="text" name="search_group_name">
        <br/>
        <label>트렌드를 볼 검색어 목록(여러개의 검색어의 경우 ','로 구분한다</label>
        <input type="text" name="search_keywords">
        <br/>
        <input type="submit" value="트렌드 보기">
    </form>
</body>
</html>


<!-- day07/naverapi/search_trend/templates/result.html -->
<!-- {{result.start_date}}
{{result.end_date}}
{{result.time_unit}}
{{result.group_name}}
{{result.keywords}} -->

{{result}}
```

```python
# day07/naverapi/boards/models.py
from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    created_by = models.CharField(max_length=10, null=True)

```

CRUD 중 C
```shell
> python manage.py shell
>>> from boards.models import Board
>>> Board
>>> b1 = Board()
>>> b1.title = '첫번째 제목'
>>> b1.contents = '여기는 컨텐츠'
>>> b1.creator = 'Me'
>>> print(b1.title)
>>> print(b1.contents)
>>> print(b1.creator)
>>> b1.save()

>>> b2 = Board()
>>> b2.title = '수업'
>>> b2.contents = '-'
>>> b2.creator = '^O^'
>>> print(b2.title)
>>> print(b2.contents)
>>> print(b2.creator)
>>> b2.save()

>>> Board.objects.all() -> 전체리스트 출력
>>> Board.objects.filter(title='첫번째 제목') -> 검색
>>> Board.objects.filter(title='첫번째 제목').first()
>>> b1 = Board.objects.filter(title='수업')[0]
>>> print(b1.title)
>>> print(b1.contents)
>>> print(b1.creator)

>>> b_all = Board.objects.all()
>>> for b in b_all:
...     print(b.title)
```