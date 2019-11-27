# python
python15

11.26


### JS,jQuery
* 요소를 찾아서
* 요소에 이벤트가 발생하는 것을 포착해서(Event Listener)
* 이벤트가 발생했을 때 어떤 로직을 실행할 지 결정(Ebent Handler)


### AJAX
* 비동기 JS & XML
* Callback(실행은 다른 곳에 맡겨두고 다 완료되면 알림을 받음)
* ```html
  <script>
  $(function(){
      $.ajax({
          url: ' 어느주소로 요청을 보낼지',
          mehtod: '어떤 request method로 보낼지',
          data: {
              key: '어떤 형태로 보낼지'
          },
          success: function(data){
              '요청이 성공적으로 완료됐을때(Callback)'
          },
          error: function(data){

          }
      })
  })
  </script>
  ```

* 이벤트 발생(두가지 방법)
  - JS로 HTML 요소를 추가한 다음, AJAX로 서버에 요청을 보내 실제 DB에 반영
  - AJAX로 서버에 요청을 보내 실제 DB에 반영되고 나면 JS로 HTML요소 추가, 성공 response가 올때까지 반영X

* 댓글수정
  * 수정 버튼을 누른다.
  * 원래의 댓글 내용이 입력창에 들어간다.
  * 확인버튼을 누르면 수정한 내용이 반영된다.
    * 방법 1
      확인 버튼에 속성을 추가해서 제출할 때 해당 속성에 유무를 파악해 서로 다른 로직을 탈 수 있도록 한다.
    * 방법 2
      수정할 때 ajax로 제출하는 url부분을 변수(HTML 속성)로 만들어서 처리
      
      

### Auth(User)

```shell
> python manage.py createsuperuser
```

localhost:8000/admin
이미 login, logout,signup 모델링이 되어있음
/accounts/login
/accounts/logout
/accounts/signup

```shell
> python manage.py startapp accounts
```

> HTTP req/res -> 무상태성 : 한번 주고 난 이후에는 모르는 사이, 너가 로그인 했는지 안했는지 모른다.
> 정보저장 주체의 차이 / 라이프사이클 (cookie vs session)
>   * cookie : 내 브라우저, 정보의 위치, 종료되어도 유지
>   * session : 서버 컴퓨터, 끄면 날아감