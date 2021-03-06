# board/urls.py
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('<int:article_id>/', views.article_detail, name="article_detail"),
    path('new/', views.new_article, name="new_article"),
    path('<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('<int:article_id>/comments/new/', views.new_comment, name='new_comment'), # board/1/comments/new/
    path('<int:article_id>/like/', views.toggle_like, name="toggle_like"), # board/1/like/
]
