# python
11.08

* parameter
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

* html 파일로 view 만들기(render template)

* Beautiful soup
  * 사이트 구조 분석하는 방법(html 방법)
  * URL 구조(query string) 분석하는 방법
  * 사람인 크롤링
  * 데이터가 xml 형태로 주고받는 사이트 제외 모두 크롤링 가능(로그인 안한 상태)
  * (따로 찾아보기 : beautiful soup xml)





------





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

```python

```

