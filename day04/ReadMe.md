# python
python04

11.11

### Remind
* Chrome 개발자 도구 Network 탭 보는 법
* Network탭과 Elements 탭을 분석해서 여러 사이트 크롤링하는 방법
  * 파라미터 만들어서 서버로부터 원하는 자료 가져오기
  * 크롤링 할 때 일반 클라이언트인 척 해보기
  * CSRF Token -> POST
  * 요청 보내서 받은 데이터를 다시 파싱해서 새로운 URL로 요청 보내기

### 지난주 과제
* 사람인 크롤링 했던거 세부정보 크롤링하기
* 다음웹툰도 웹툰 세부정보 크롤링하기
    각 요일별 웹툰 데이터 -> 월, 화, 수... -> 각 요일 웹툰 리스트 -> 해당 웹툰의 세부정보
    ```python
    # app.py

    from flask import Flask, request, render_template
    import requests
    import json
    
    app = Flask(__name__)
    # $env:FLASK_ENV="development"
    # $env:FLASk_DEBUG="True"
    # flask run
    
    # 1. 전체 요일 적혀있는 페이지
    @app.route('/')
    def index():
        days = {
            '월요일':'mon',
            '화요일':'tue',
            '수요일':'wed',
            '목요일':'thu',
            '금요일':'fri',
            '토요일':'sat',
            '일요일':'sun'
        }
        return render_template('index.html', days=days)

    # 2. 각 요일에 대한 데이터 요청하는 곳
    @app.route('/<day>')
    def day_webtoon_list(day):
        url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
        response = requests.get(url)
        data = response.json()
        webtoons = {}
        for toon in data["data"]:
            webtoon_title = toon["title"]
            webtoon_nickname = toon["nickname"]
            webtoon_introduction = toon["introduction"]
            webtoon_artists = []
            for artist in toon["cartoon"]["artists"]:
                webtoon_artists.append(artist["name"])
    
            webtoons[webtoon_title] = [webtoon_nickname, webtoon_introduction, ",".join(webtoon_artists)]
    
        return render_template('day_webtoon_list.html', webtoon_dic=webtoons)
    
    # 3. 각 웹툰에 대한 세부 데이터 요청하는 곳
    @app.route('/webtoon/<nickname>')
    def webtoon_info(nickname):
        url = f'http://webtoon.daum.net/data/pc/webtoon/view/{nickname}'
        return requests.get(url).json()
    ```
    ```html
    <!-- index.html -->
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        {% for key, value in days.items(): %}
            <a href="/{{ value }}">{{ key }}</a><br/>
        {% endfor %}
    </body>
    </html>

    <!-- day_webtoon_list.html -->
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        {% for key, value in webtoon_dic.items(): %}
            <a href="/webtoon/{{value[0]}}">{{ key }}</a> / {{ value[1] }} / {{ value[2] }} <br/>
        {% endfor %}
    </body>
    </html>
    ```


### Form 데이터 처리하기
* path param
  * Fake 검색창(query String) : 검색창 + 검색결과
  * Fake Login : 로그인창 -> 로그인로직 -> 메인창
    ```python
    from flask import Flask, request, render_template, redirect, url_for
    import requests
    import json
    
    app = Flask(__name__)
    # $env:FLASK_ENV="development"
    # $env:FLASk_DEBUG="True"
    # flask run
    
    
    # Form data
    @app.route('/naver')
    def fake_naver():
        return render_template('naver.html')
    
    @app.route('/naver/search')
    def fake_naver_search():
        # 검색 로직
        query = request.args.get('query')
    return render_template('search.html', q = query)

    @app.route('/login')
    def login_form():
        # 아이디 입력창, 패스워드 입력창, 로그인 버튼
        return render_template('login.html')
    
    @app.route('/login/submit', methods=['POST'])
    def login():
        # 아이디를 조회하고, 해당 row의 비밀번호가 일치하는지 확인
        # 로그인 로직
        # return render_template=['success.html]
        return redirec/t(url_for('main'))
    
    @app.route('/main')
    def main():
        return '로그인에 성공하셨습니다. 메인페이지 입니다.'
    ```
    ```html
    <!-- naver.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <!-- form태그를 이용해서 검색창(검색어 입력, 검색 버튼) 만들기 -->
        <form action="/naver/search" method="GET">
            <input type="text" name="query">
            <input type="submit">
        </form>
    </body>
    </html>

    <!-- search.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        '{{ q }}'에 대한 검색 결과입니다.
    </body>
    </html>

    <!-- login.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <form action="/login/submit" method="POST">
            ID <input type="text"><br/>
            PWD<input type="password"><br/>6
            <input type="submit">
        </form>
    </body>
    </html>

    <!-- success.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <p>로그인에 성공하셨습니다.</p>
    </body>
    </html>
    ```

### Django 입문
(https://tutorial.djangogirls.org/ko/)
```
> pip install django
> django-admin startproject myapp
> cd ./myapp
> python manage.py runserver
> http://localhost:8000
> python manage.py migrate
```


* 장고의 파일구조 살펴보기
  * 프로젝트 > 어플리케이션

    * settings.py
    * urls.py -> route 관리
    * django는 기본으로 admin 제공
  
    ```python
    > python manage.py startapp webtoon 

    # settings.py
    LANGUAGE_CODE = 'ko'  
    TIME_ZONE = 'Asia/Seoul'
    ```
  
* ORM 빼고 새로운 프로젝트 진행

### 아이디어톤 이후에 CRUD -> ORM
### 다음주 CRUD로 프로젝트 진행


----------------------


Flask - WAS(Web Application Server)
Flask(경량화) -> Django(중규모)

REST API - https://meetup.toast.com/posts/92
Creat - Post(생성, /webtoons)
Read - Get (하나를 조회, /webtoons, /webtoon/<nickname>)
Update - Put, Patch(/webtoon/<nickname>)
Destroy - Delete(/webtoon/<nickname>)

> www.naver.com에 접속했을 때 발생하는 모든 과정
> 클라이언트 url -> DNS에서 url을 ip로 치환(변환) -> request -> route(mapping) -> **controller** <-> model
> **controller** -> view -> response -> Browser -> HTML -> DOM Tree -> Render
