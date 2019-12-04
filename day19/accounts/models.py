from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 여러 정보 담기
    address = models.CharField(max_length=200)