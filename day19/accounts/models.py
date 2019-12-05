from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 여러 정보 담기
    address = models.CharField(max_length=200)
    fans = models.ManyToManyField('self', related_name='stars')
    # self는 클래스, settings.AUTH_USER_MODEL, on_delete=models.CASCADE