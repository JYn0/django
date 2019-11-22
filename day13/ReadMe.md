# python
python13

11.22

### JS + jQuery
* css Selector(.className, #ID)
* Event
* Dom
* 사용 이유
  * 페이지를 다이나믹하게 만들기 위해서 사용
  * 클라이언트 단에서 데이터(상태)를 관리
  * 요소 찾기 -> 해당 요소에 이벤트 먹이기
    이벤트 발생 -> 어떠한 변화가 생김(색상이 바뀌거나 생성,소멸 등의 여러 변화)
  * (ajax) 일부 부분에서 발생한 변화를 서버에 저장, 수정, 삭제


script tag는 body tag 끝나기 전에 넣어주는게 좋음
JS파일은 큰 경우가 많기 때문
모든 돔트리가 완성되고, 이벤트를 돔트리에 넣는 것이 좋음

```python
# instagram/article/urls.py
urlpatterns = [
    path('js-test/', article_views.js_test),
]

```

F12 console
```shell
> console.log("Hello World!")
  # 변수 확인용
> alert("알람!")
  # 확인버튼을 누르기 전까지 중지, 데이터 잘 왔는지 확인할 때
> confirm("확인(True) or 취소(False)")
< true(확인)
  # if문이나 로그아웃 사용시
> prompt("입력창에 대답하시오")
< "넹"
  # 잘사용하지않음

# document 파일은 날라온 모든 파일
> console.log(document)
# 열고있는 창, 최상위
> console.log(window)

> window.alert("hi");
> window.close();
> window.location.href
< 주소

```


```shell
요소 찾는 방법

> document.getElementById('joke')
< <h2 id=​"joke">​JS 재미없음​</h2>

> document.getElementsByClassName('element')
< HTMLCollection(5) [p.element, p.element, p.element, p.element, p.element]
  Elements는 배열

> document.getElementsByTagName('p')
< HTMLCollection(5) [p.element, p.element, p.element, p.element, p.element]

> document.querySelector('.class_name')
querySelector는 하나만 찾아줌
> document.querySelectorAll('.element')
< NodeList(5) [p.element, p.element, p.element, p.element, p.element]

```


> JS는 주로 camelCase
> camelCase vs snake_Case


* addEventListener와 Handler

script에서 `여러 줄을 받을 수 있음` -> ``

JavaScript는 eventListener안생긴다.
document부터 찾아서 하기