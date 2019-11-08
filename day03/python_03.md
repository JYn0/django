# python
11.08

* parameter
  ```python
  # 첫 준비
  from flask import Flask, request, render_template
  
  app = Flask(__name__)
  if __name__ == '__main__':
      app.run(debug=True)
  # $env:FLASK_ENV="Develpment"
  # $env:FLASK_DEBUG="Develpment"
  
  @app.route('/')
  def index():
      return {'hello':'hi'}
  
  # > flask run
  # http://localhost:5000/
  # {
  # hello: "hi"
  # }
  ```
  * query string
  
    url?(파라미터이름=값)&(파라미터이름=값)&...
  
    값이 너무 길어지면 안됨
  
    ```python
      # app.py
      # query string 방식
      from flask import Flask, request, render_template
      
      app = Flask(__name__)
      if __name__ == '__main__':
          app.run(debug=True)
      
      @app.route('/')
      def index():
          # request.args.get('파라미터명')
          # request.args -> flask가 client로부터 받은 파라미터를 담는 Dictionary(Immutable)
          student = request.args.get('student')
          return {'hello': student}
      
      # student 값을 바꿔주면서
      # 주소창 뒤에 쓰는 이름으로 출력됨
      # http://localhost:5000/?student=jy
      # {
      # hello: "jy"
      # }
    ```
  
      
  
  * path parameter
  
    ```python
    # 주소 자체에 parameter 심어놓기
    @app.route('/<day>')
    def toons(day):
        return{ 'today is': day}
    # http://localhost:5000/mon
    # {
    # today is: "mon"
    # }
    ```
  
    +) python flask how to get multiple parameter from url
  
    
  
* 웹툰 데이터를 요일별로 다르게 url 세우기
  ```python
  from flask import Flask, request, render_template
  import requests
  
  app = Flask(__name__)
  if __name__ == '__main__':
      app.run(debug=True)
  
  @app.route('/daum_webtoon')
  def daum_toon_index():
      html = '''
          <a href="/daum_webtoon/mon">월요일</a>
          <a href="/daum_webtoon/tue">화요일</a>
          <a href="/daum_webtoon/wed">수요일</a>
          <a href="/daum_webtoon/thu">목요일</a>
          <a href="/daum_webtoon/fri">금요일</a>
          <a href="/daum_webtoon/sat">토요일</a>
          <a href="/daum_webtoon/sun">일요일</a>
      '''
      return html
  # http://localhost:5000/daum_webtoon
  
  @app.route('/daum_webtoon/<day>')
  def daum_toon(day):
      url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
      data = request_json_data_from_url(url)
      return { day: parse_daum_webtoon_data(data)}
  
  def request_json_data_from_url(url):
      response = requests.get(url)
      data = response.json()
      return data
  
  def parse_daum_webtoon_data(data):
      # data parsing
      toons = []
      for toon in data["data"]:
          title = toon["title"]
  
          desc = toon["introduction"]
  
          genres = []
          for genre in toon["cartoon"]["genres"]:
              genres.append(genre["name"])
  
          artists = []
          for artist in toon["cartoon"]["artists"]:
              artists.append(artist["name"])
          
          img_url = toon["pcThumbnailImage"]["url"]
          tmp = {
              title:{
                  "desc":desc,
                  "writer":artists,
                  "genres":genres,
                  "img_url":img_url
              }
          }
          toons.append(tmp)
      return toons
  
  # http://localhost:5000/daum_webtoon/mon
  ```
  
  
  
* html 파일로 view 만들기(render template)
  app.py과 같은 레벨에 templates폴더만들고 폴더안에 html 만들기
  
  ```python
  @app.route('/daum_webtoon')
  def daum_toon_index():
  return render_template('daum_webtoon_list.html')
  # http://localhost:5000/daum_webtoon
  ```
  ```html
  <!-- daum_webtoon_list.html -->
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <a href="/daum_webtoon/mon">월요일</a>
      <a href="/daum_webtoon/tue">화요일</a>
      <a href="/daum_webtoon/wed">수요일</a>
      <a href="/daum_webtoon/thu">목요일</a>
      <a href="/daum_webtoon/fri">금요일</a>
      <a href="/daum_webtoon/sat">토요일</a>
      <a href="/daum_webtoon/sun">일요일</a>
  </body>
  </html>
  ```
  
  ```html
  <!-- daum_webtoon_list.html -->
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <!-- {% python logic %} -->
      {% for day in days %}
          <a href="/daum_webtoon/{{ day }}">{{ day }}</a>
      {% endfor %}
      {{ msg }}
  </body>
  </html>   
  ```
  
  ```python
  # app.py
  @app.route('/daum_webtoon')
  def daum_toon_index():
      days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
      msg = "아... 집가고싶다"
      msg2 = "배고프다"
      # **locals() -> 값 넘겨주기
      # days=days -> days만 넘겨주기 원하는 데이터만 template에 넘겨주기, 여러개 보낼 수 있음
      return render_template('daum_webtoon_list.html', days=days, msg=msg)
  # http://localhost:5000/daum_webtoon
  ```
  
  




* Beautiful soup
  * 사이트 구조 분석하는 방법(html 방법)
  * URL 구조(query string) 분석하는 방법
  * 사람인 크롤링
  * 데이터가 xml 형태로 주고받는 사이트 제외 모두 크롤링 가능(로그인 안한 상태)
  * (따로 찾아보기 : beautiful soup xml)

  ```python
  # > pip install bs4

  from bs4 import BeautifulSoup
  import requests

  url = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&panel_type=&search_optional_item=n&search_done=y&panel_count=y"
  response = requests.get(url)
  print(response)
  # <Response [200]>
  
  ```
    * find
      * find
      * find_all
    * select
      * select
      * select_one

  ```python
  # saramin_parse.py
  
  from bs4 import BeautifulSoup
  import requests
  
  url = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&panel_type=&search_optional_item=n&search_done=y&panel_count=y"
  response = requests.get(url)
  # print(response)
  # print(response.text)
  
  html = BeautifulSoup(response.text, 'html.parser')
  
  # company_name class 찾기
  company_names = html.select('.company_name')
  recruit_names = html.select('.recruit_name')
  recruit_conditions = html.select('.list_recruit_condition')
  
  '''
  for company_name in company_names:
      # print(company_name)
      print(company_name.text)
  for recruit_name in recruit_names:
      print(recruit_name.text)
  print(len(company_names))
  print(len(recruit_names))
  '''
  for company_name,recruit_name, condition in zip(company_names, recruit_names, recruit_conditions):
      print(f'{company_name.text}- {recruit_name.text}')
      print(condition.text)
  ```
  
  ```python
      # 위와 동일(상위 class를 가져와서 찾기)
    company = html.select('.part_top')
    for com in company:
      print(f'{com.select_one(".company_name").text}- {com.select_one(".recruit_name").text}')
      print(com.select_one('.list_recruit_condition').text)
  ```
  
  ```python
  my_query = {
    'All' : {
        'name': 'cat_cd',
        'webAll': '404'
    },
    'position': {
        'name': 'cat_key',
        'IOS': '40701'
    }
  }

  my_url = f'http://www.saramin.co.kr/zf_user/jobs/list/job-category?{my_query["All"]["name"]}={my_query["All"]["webAll"]}&panel_type=&search_optional_item=n&search_done=y&panel_count=y'
  my_response = requests.get(my_url)
  my_html = BeautifulSoup(my_response.text, 'html.parser')
  my_company = my_html.select('.part_top')
  for my_com in my_company:
    print(f"{my_com.select_one('.company_name').text}- {my_com.select_one('.recruit_name').text}")
    print(my_com.select_one('.list_recruit_condition').text)

  ```

  ```python
  # 2차 크롤링
  from bs4 import BeautifulSoup
  import requests
  
  url = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&panel_type=&search_optional_item=n&  search_done=y&panel_count=y"
  response = requests.get(url)  
  html = BeautifulSoup(response.text, 'html.parser')

  company_list = html.select('ul.product_list li') # product_list 안에 있는 li
  for com in company_list:
      # a tag 한번 더 찾기, href 속성 값
      idx = com.select_one('a')['href'].split('=')[-1]
      company_info_url = 'http://www.saramin.co.kr/zf_user/jobs/relay/view-ajax'
      company_info_params = { 'rec_idx': idx }
      company_response = requests.post(company_info_url, params=company_info_params)
      print(company_response)
      company_html = BeautifulSoup(company_response.text, 'html.parser')
      company_title = company_html.select_one('a.company').text
      print(company_title.strip())
  
      break
  ```



  
------




* 사람인 나머지 데이터 파싱
* 다음웹툰(url 분석, ditionary) 일요일 첫번째 나오는 웹툰 상세보기 페이지 크롤링
  * url 따는거 -> 웹툰을 돌아다니면서 달라지는 부분 확인, 달라지는 내용이 어디에 있는지 찾아보기