# python

11.06

>  req.py
>
> req2.py

<head>
    기본 정보
</head>



og tag

-> 미리보기, 관련 검색어 뜨기, search engine 최적화

웹마스터도구





window+r -> powershell



webtoon.daum.net의 xhr 가져오기



http://webtoon.daum.net/data/pc/webtoon/list_serialized/wed

```python
# req.py
# 1. 요청을 보내기 위한 requests 모듈을 import 한다.
# 모듈이 없을 경우 'pip install requests'를 실행
import requests

# 2. 요청을 보내기 위한 url을 변수에 저장한다.
url = "http://webtoon.daum.net/data/pc/webtoon/list_serialized/wed"

# 3. 해당 url에 요청을 보낸다.
response = requests.get(url)

# 4. 응답을 출력한다.
print(response)
```



* 응답코드

  200~ 정상

  300~ 리디렉션

  400~ 클라이언트 오류(사용자 책임)

  ​	404:URL 찾을 수 없음

  ​	403:Forbidden

  ​	401:권한없음

  500~ 서버오류(개발자 책임)



```python
# req2.py

# 1. 요청을 보내기 위한 requests 모듈을 import 한다.
import requests

# 2. url에 주소를 저장한다.
url = "https://ticket.melon.com/offer/ajax/offerList.json?offerPosType=MAIN_B_CO_1"

# 3. 요청을 보내고 응답을 변수에 저장한다.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
response = requests.get(url, headers=headers)

# 4. 변수에 저장된 내용을 출력한다.
print(response.text)


# (추가사항) 5. new! 공연, 2019 전국투어, 뮤지컥&연극 각 부분을 출력해보기
# https://ticket.melon.com/offer/ajax/offerList.json?offerPosType=MAIN_B_CO_2
# https://ticket.melon.com/offer/ajax/offerList.json?offerPosType=MAIN_B_CO_3
```

