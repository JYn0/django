# python
python02

11.07

> app.py
> dictionary.py
> ws1107.py

* 파이썬 딕셔너리(Dictionary)
  * 딕셔너리란(Hash, HashMap)

    key값과 value값으로 한쌍의 묶음을 저장하는 것

    key값은 고유(중복된 값이 있으면 나중에 들어온 값으로 변경)

    똑같은 key값에 value를 추가하면 그 전 데이터 날라가버림

    

  * 쓰는 이유

    딕셔너리안에 딕셔너리 가능

    key값 하나에 value 값 여러개 담을 수 있음

    

  * 활용 방법

  * JSON과 비교, 차이점

  * 딕셔너리 활용 문제

* 크롤링으로 원하는 정보 추출

* 자유롭게 원하는 사이트에서 데이터 뽑기

* 함수 활용하기

* 플라스크 기본

  ```python
  > pip install flask
  # app.py
  from flask import Flask, escape, request
  
  app = Flask(__name__)
  if __name__ == '__main__':
      app.run(debug=True)
  # $env:FLASK_ENV="development"
  # $env:FLASk_DEBUG="True"
  @app.route('/')
  def index():
      return { 'method': 'Hello'}
  
# -----------------------------------------------------
  
from flask import Flask, escape, request
  import json
  import requests
  
  app = Flask(__name__)
  if __name__ == '__main__':
      app.run(debug=True)
  # $env:FLASK_ENV="Develpment"
  # $env:FLASK_DEBUG="Develpment"
  @app.route('/')
  def index():
      daily_toon_data = {}
      day = 'mon'
      url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
      data = request_json_data_from_url(url)
      daily_toon_data[day] = parse_daum_webtoon_data(data)
      # print(daily_toon_data[day])
      
      return daily_toon_data
  
  
  def request_json_data_from_url(url):
      # data 크롤링
      # 해당 url에 요청 보내기
      response = requests.get(url)
      data = response.json()
      return data
  
  def parse_daum_webtoon_data(data):
      # data parsing
      toons = []
      for toon in data["data"]:
          # 제목의 key는 'title'
          title = toon["title"]
  
          # 설명의 key는 'introduction'
          desc = toon["introduction"]
  
          # 장르의 위치는 'cartoon'안에 'genre'리스트 안에 'name' key
          genres = []
          for genre in toon["cartoon"]["genres"]:
              genres.append(genre["name"])
          # print(genres)
  
          # 작가의 위치는 'cartoon'안에 'artists'리스트 안에 'name' key
          artists = []
          for artist in toon["cartoon"]["artists"]:
              artists.append(artist["name"])
          # print(name)
          
          # 썸네일 이미지의 위치는 'pcThumbnailImage'리스트 안에 'url'key
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
          # print(toons)
      return toons
  ```
  
  
  

JSON Viewer Chrome 추가



### Quiz

```python
# ws1107.py
# 배열의 길이를 구하는 함수는 len(배열)
# 반올림 하는 함수는 round(숫자, 소숫점)
# 1. 평균을 구하세요.
score = {
    "수학": 90,
    "영어": 87,
    "한국지리": 92
}

size = len(score)
avg = 0
for tmp in score.values():
    avg += tmp
print(avg)
avg = avg/size
print(round(avg,1))

'''
if 조건1:
    a
elif 조건2:

else:
    a

'''

# 2. 각 학생의 평균 점수와 반 평균을 구하세요.
scores = {
    "a학생": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "b학생": {
        "수학": 100,
        "국어": 70,
        "음악": 80
    },
}

size = len(scores["a학생"])
avg_a = 0
for tmp in scores["a학생"].values():
    avg_a += tmp
print(avg_a)
avg_a = avg_a/size
print(round(avg_a,1))

size = len(scores["b학생"])
avg_b = 0
for tmp in scores["b학생"].values():
    avg_b += tmp
print(avg_b)
avg_b = avg_b/size
print(round(avg_b,1))



for tmp1 in scores.values():
    for tmp2 in tmp1.values():
        avg += tmp2
print(avg)
avg = avg/size
print(round(avg))

```



```python
# dictionary.py
# 3. 다음 웹툰의 금요일 웹툰 전체의 리스트 중에서 각 웹툰의 제목, 설명, 작가 이름, 장르, 썸네일 이미지(주소)만 골라 새로운 dictionary를 만들고, 이 dictionary를 담고있는 list를 만드세요.

# 3번

url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/fri"

response = requests.get(url)
data = response.json()
# print(data)
# print(type(data))

# for d in data.keys():
#     print(d)
#print(type(data["data"])) # list
webtoon_data = data["data"]

toons = []

for toon in webtoon_data:
    # 제목의 key는 'title'
    title = toon["title"]

    # 설명의 key는 'introduction'
    desc = toon["introduction"]

    # 장르의 위치는 'cartoon'안에 'genre'리스트 안에 'name' key
    genres = []
    for genre in toon["cartoon"]["genres"]:
        genres.append(genre["name"])
    # print(genres)

    # 작가의 위치는 'cartoon'안에 'artists'리스트 안에 'name' key
    artists = []
    for artist in toon["cartoon"]["artists"]:
        artists.append(artist["name"])
    # print(name)
    
    # 썸네일 이미지의 위치는 'pcThumbnailImage'리스트 안에 'url'key
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
print(toons)


3-1. 금요일 뿐만 아니라 월요일부터 일요일까지의 웹툰 데이터를 파싱해서 각각 dictionary로 만드세요
import json
import requests
import time
# 3-1

'''
def 함수명(파라미터):
    함수만들기
'''

def request_json_data_from_url(url):
    # data 크롤링
    # 해당 url에 요청 보내기
    response = requests.get(url)
    data = response.json()
    return data

def parse_daum_webtoon_data(data):
    # data parsing
    toons = []
    for toon in data["data"]:
        # 제목의 key는 'title'
        title = toon["title"]

        # 설명의 key는 'introduction'
        desc = toon["introduction"]

        # 장르의 위치는 'cartoon'안에 'genre'리스트 안에 'name' key
        genres = []
        for genre in toon["cartoon"]["genres"]:
            genres.append(genre["name"])
        # print(genres)

        # 작가의 위치는 'cartoon'안에 'artists'리스트 안에 'name' key
        artists = []
        for artist in toon["cartoon"]["artists"]:
            artists.append(artist["name"])
        # print(name)
        
        # 썸네일 이미지의 위치는 'pcThumbnailImage'리스트 안에 'url'key
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
        # print(toons)
    return toons


days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
daily_toon_data = {}

for day in days:
    print(day)
    url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
    data = request_json_data_from_url(url)
    daily_toon_data[day] = parse_daum_webtoon_data(data)
    print(daily_toon_data[day])
    time.sleep(3)
  
```





> 덕타이핑(duck)
>
> 형을 지정하지 않았는데 메소드를 사용할 수 있으면 그 변수는 그 메소드를 사용하는 형이 됨