from django.db import models
from faker import Faker
f = Faker()

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    keyword = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy(cls, n):
        # article = cls()
        # article.title = '~~'
        # article.content = 
        # ...
        # article.save()

        # cls : 자신, 위의 내용을 줄인 것
        for i in range(n):
            cls.objects.create(
                title= f.text(20),
                content= f.text(),
                keyword= f.company(),
                email= f.email(),
            )

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
