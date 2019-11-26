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

### Auth(User)