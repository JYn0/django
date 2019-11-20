# python
python11

11.20

### Instagram
* 댓글(comment): model(모델링), url(설정)
  * database relation(1:N)
    > 1:N
    > user / 게시글(user에 대한 정보를 가지고 있음 -> ID)
    > user는 게시글을 모름, 게시글을 user를 알고있음
    > user의 ID로 게시글을 검색하면 user가 어떤글을 썼는지 알수있음

* 이미지 업로드, 좋아요
  * 좋아요, 해시태그: database relation(M:N)

```shell
> django-admin startproject instagram
> cd instagram
> python manage.py startapp article
settings.py 작성
urls.py 작성
instagram/article/urls.py 만들고 작성
views.py에 def 써주기
models.py
def에 필요한 templates 폴더 만들어서 html 작성
```

> {% %} -> 파이썬 로직
> {{ }} -> 실제 출력(내용, 태그 등)

```python
# index.html
{% for comment in article.comment_set.all %}
->
{% for comment in article.comments %}
# models.py
def comments(self):
    def comments(self):
        # article_id가 self.id인 것을 return해라
        return Comment.objects.filter(article_id=self.id)
```