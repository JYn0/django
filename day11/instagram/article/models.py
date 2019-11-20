from django.db import models

# Create your models here.

class Article(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def comments(self):
        # article_id가 self.id인 것을 return해라
        return Comment.objects.filter(article_id=self.id)

# python manage.py makemigrations -> 틀을 만듦
# python manage.py migrate -> 실제 테이블을 만들어줌

class Comment(models.Model):
    # Article 하나가 여러개의 Comment를 갖는다(1:N)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # on_delete:옵션, CASCADE -> 게시글이 삭제되면 댓글도 삭제되어야함