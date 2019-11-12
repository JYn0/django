# python
11.12

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
      > ex)게시판이라면, Post라는 app을 만들어서 그 안에서 모든 내용을 처리한다.
    ``` python
    > django-admin startproject day5
    > cd day5
    > python manage.py startapp lotto
    # settings.py
    LANGUAGE_CODE = 'ko'
    TIME_ZONE = 'Asia/Seoul'
    ```
* 로또 번호 생성기 + 번호 체크 + 번호를 몇개 뽑을지