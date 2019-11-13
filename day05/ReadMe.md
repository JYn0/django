# python
python05
11.12

> day5/
> lotto/
> ascii/
> opgg/

### Django 시작하기
* 프로젝트 만들기
  * 프로젝트 vs 어플리케이션(app)
  * MVC -> MVT
  * Model View Controller -> Model View(Controller 역할) Template(View 역할)
  * Django
    * 시작하기
      ```
      > django-admin startproject projectname
      > cd myproject
      > python manage.py startapp appname
      ```
      > project(가장 바깥 개념, 가장 큰 단위)
      > django에서 app단위는 하나의 모델에 대한 모든 내용이 담겨있다.
      > app하나당 기능 하나
      > ex)게시판이라면, Post라는 app을 만들어서 그 안에서 모든 내용을 처리한다.
  
* 로또 번호 생성기 + 번호 체크 + 번호를 몇개 뽑을지
  * 메인 페이지(번호를 몇개 뽑을지, 생성버튼)
    -> '/lotto'
  * 결과 페이지(랜덤으로 뽑힌 번호, 뽑힌 번호가 가장 최근 당첨번호와 몇개가 일치하는지)
    -> '/lotto/winning'

  ``` python
  > django-admin startproject day5
  > cd day5
  > python manage.py startapp lotto
  # settings.py
  LANGUAGE_CODE = 'ko'
  TIME_ZONE = 'Asia/Seoul'
  INSTALLED_APPS = [
  'lotto' # 추가
  ]  
  # urls.py
  # 사용자로부터 request가 들어오면 urls파일이 어느 views에 어느 method로 갈지 설정
  from lotto import views  
  # views.py
  # django에서 첫번째 param은 request
  def lotto(request):
  return render(request,'lotto.html') # <- 규칙  
  # lotto/templates폴더 -> html
  ```
  
  ```python
  # views.py

  from django.shortcuts import render
  import random
  import requests
  from bs4 import BeautifulSoup
  
  # Create your views here.
  
  # django에서 첫번째 param은 request
  def lotto(request):
      return render(request,'lotto.html')
  
  def winning(request):
      # 1. 1~45까지의 숫자 중 n개의 숫자 랜덤 추출
      # 1-1 1~45 번호를 가진 배열 만들고
      num_list = list(range(1,46))
      # range(시작숫자, 끝숫자(불포함))
      # random.sample을 사용하기 위해 list
      num_count = request.GET['count']
  
      # 1-2 해당 배열에서 count만큼의 숫자를 샘플링
      result = random.sample(num_list, int(num_count))
      result.sort()
  
      # 2. 로또 당첨번호 공개 사이트로 가서 지난주 당첨 정보 가져오기
      # - 몇 회차인지, 언제 당첨번호인지, 1등 당첨금이 얼마인지
  
      url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
      response = requests.get(url)
      html = BeautifulSoup(response.text, 'html.parser')
      winning_numbers = html.select('div.win span')
      winning_count = 0
      winning_list = []
      for number in winning_numbers:
          # result list 변수에 number가 포함되어 있는지
          winning_list.append(int(number.text))
          if int(number.text) in result: # element가 list에 들어갔있는지 check
              winning_count += 1
  
      return render(request,'winning.html', {'result': result, 'winning_list':   winning_list, 'winning_count': winning_count})
  ```

  ```html
  <!-- templates/lotto.html -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h1>몇개의 번호를 추첨하시겠습니까?</h1>
      <form action="/lotto/winning">
          <select name="count">
              <option value="1">1개</option>
              <option value="2">2개</option>
              <option value="3">3개</option>
              <option value="4">4개</option>
              <option value="5">5개</option>
              <option value="6">6개</option>
          </select>
          <input type="submit">
      </form>
  </body>
  </html>

  <!-- templates/winning.html -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h1>당신의 추첨 번호는
      {% for num in result %}
          <span>{{ num }}</span> / 
      {% endfor %}
      </h1>
        
      <h3>
          지난주 추첨번호는
          {% for num in winning_list %}
              <span>{{num}}</span> / 
          {% endfor %}
      </h3>
      <h3>추첨번호와 일치 하는 숫자는 {{winning_count}}개 입니다.</h3>
  </body>
  </html>  
  ```


* :star: app 만드는 순서​
  1. python manage.py startapp appname
  2. settings.py의 INSTALLED_APPS에 만든 app 추가
  3. 만든 app 폴더에 가서 `views.py` 파일에 함수 등록
  4. 해당 함수의 결과로 return할 template 선언
  5. 위 template파일 만들기
  6. `urls.py` 에 등록된 함수 연결  



* ascii(http://artii.herokuapp.com/)
```python
> python manage.py startapp ascii

# settings.py
INSTALLED_APPS = ['ascii']

# urls.py
from ascii import views as ascii_views

urlpatterns = [
    path('ascii/', ascii_views.ascii),
    path('ascii/result/', ascii_views.result)
]
```

```python
# views.py
from django.shortcuts import render
import requests

# Create your views here.
def ascii(request):
    # main page
    # 입력하고자 하는 text를 받아야함
    # artii에서 제공하는 폰트 중 선택
    url = 'http://artii.herokuapp.com/fonts_list'
    response = requests.get(url)
    fonts_list = response.text.split('\n')
    # fonts_list -> array type, \n로 split해서 배열에 저장
    context = {
        'fonts' : fonts_list
    }
    return render(request, 'ascii.html', context)

def result(request):
    # ascii에서 입력한 텍스트와 폰트를
    # artii에 보내서 결과를 받아서 보여줌
    font = request.GET['font']
    text = request.GET['text']
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    response = requests.get(url)
    context = {
        'result': response.text
    }
    return render(request, 'result.html', context)
```
`ascii/templates`
```html
<!-- ascii.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>text와 font를 입력하세요</h1>
    <form action="/ascii/result">
        <input type="text" name="text">
        <select name="font">
            {% for font in fonts %}
            <option value= "{{font}}">{{font}}</option>
            {% endfor %}
        </select>
        <input type="submit" value="아스키 아트 만들기">
    </form>
</body>
</html>

<!-- result.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <pre>{{result}}</pre>
</body>
</html>

```

* opgg
  ```python
  > python manage.py startapp opgg
  # settings.py
  INSTALLED_APPS = [
    'opgg'
  ]

  # urls.py
  from opgg import views as opgg_views
  urlpatterns = [
    path('opgg/', opgg_views.opgg),
    path('opgg/result', opgg_views.result)
  ]
  ```
  ```python
  # views.py
  from django.shortcuts import render
  import requests
  from bs4 import BeautifulSoup
  
  # Create your views here.
  def opgg(request):
      # 소환사명 입력창
      return render(request, 'opgg.html')
  
  def result(request):
      # 실제 op.gg를 크롤링해서 입력된 소환사에 대한 전적 정보를 가져온다.
      name = request.GET['nickname']
      url = f'https://www.op.gg/summoner/userName={name}'
      response = requests.get(url)
      html = BeautifulSoup(response.text, 'html.parser')
  
      if html.select_one('span.WinLose .wins') is None: # None type
          result = {
              'msg':'소환사가 없거나 언랭입니다.'
          }
      
      else: 
          result = {
              'name': name,
              'win': html.select_one('span.WinLose .wins').text,
              'lose': html.select_one('span.WinLose .losses').text,
              'ratio': html.select_one('span.WinLose .winratio').text
          }
  
      return render(request, 'ratio.html', result)
  ```
  ```html
  <!--  opgg.html -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h1>소환사를 입력하세요</h1>
      <form action="/opgg/result">
          <input type="text" name="nickname">
          <input type="submit" value="검색하기">
      </form>
  </body>
  </html>

  <!-- raio.html -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h1>{{msg}}</h1>
      <!-- name,win,lose,ratio값이 없으면 빈 string으로 들어감 -->
      <h1>{{name}}의 전적입니다.</h1>
      <h3>승 : {{win}}</h3>
      <h3>패 : {{lose}}</h3>
      <h3>승률 : {{ratio}}</h3>
  </body>
  </html>
  ```