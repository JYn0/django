# python
11.12

> day5/
> lotto/

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

    * app 만드는 순서
      1. python manage.py startapp appname
      2. settings.py의 INSTALLED_APPS에 만든 app 추가
      3. 만든 app 폴더에 가서 `views.py` 파일에 함수 등록
      4.  해당 함수의 결과로 return할 template 선언
      5. 위 template파일 만들기
      6. `urls.py` 에 등록된 함수 연결
  