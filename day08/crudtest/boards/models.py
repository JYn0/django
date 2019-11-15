from django.db import models

# Create your models here.
class Board(models.Model):
    objects = models.Manager()
    # Board라고 하는 table 이 만들어지고
    # ID와 title, contents, creator 컬럼이 만들어진다.
    title = models.CharField(max_length=32)
    # CharField는 반드시 max_length를 지정해줘야 한다.
    contents = models.TextField()
    creator = models.CharField(max_length=16)
