from django.contrib import admin
from .models import Article # 현재 폴더의 models에서 Article import

#  Register your models here.
# 등록하기
admin.site.register(Article)