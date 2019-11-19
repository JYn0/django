# python
python10

11.19

### CRUD 혼자서 구현하기
* project이름은 crudtest
* app 이름은 articles

```shell
> django-admin startproject crudtest
> cd crudtest
> python manage.py startapp articles
```

`settings.py` 수정
articles/안에 `urls.py` 만들고 crudtest/`urls.py`에 import
templates 만들기
models.py
views.py
html파일 만들기



### REST api

RESTful
어떤방식으로 어떤 요청을 보냈을때 무슨 일을 하는지


GET -> 조회
POST -> DB에 반영

|   역할   |   Request-Method   |   End-point   |  Views(Function)    |   기존 역할   |
| ---- | ---- | ---- | ---- | ---- |
|   Create   |   GET   |   /articles/new/   |   new   |   새글form   |
|   Create   |   POST   |   /articles/   |   new   |   ne새글 작성w   |
|   Read   |   GET   |   /articles/<id>/   |   show   |   글 하나   |
|   Read   |   GET   |   /articles/   |   index   |   전체 리스트   |
|   Update   |   GET   |   /articles/<id>/edit/   |   edit   |   수정form   |
|   Update   |   POST   |   /articles/<id>/   |   edit   |   수정 반영   |
|   Delete   |   POST(Delete)   |   /articles/<id>/delete/   |   delete   |   삭제   |

Delete -> GET방식 사용함(a태그는 GET만됨)
request-method에 따라

csrf token
POST요청은 form밖에 안됨
