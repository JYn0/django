from django.urls import path
from . import views as article_views
# 현재 폴더의 views를 import

urlpatterns = [
    path('', article_views.index, name="articles")
]