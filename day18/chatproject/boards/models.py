from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Room(models.Model):
    # 방 만들기
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=16, unique=True) # 채팅방의 고유 코드
    max_connection = models.IntegerField()
    master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 방장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # M:N 만들기(유저는 여러방에 들어갈 수 있고, 이 방에 여러 유저가있고, )
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="rooms") # 현재방의 접속인원

class Message(models.Model):
    # 메시지
    contents = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # 하나의 메시지가 하나의 방, 하나의 방에 여러 메시지
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 작성자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)