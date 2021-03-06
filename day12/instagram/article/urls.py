from django.urls import path
from . import views as article_views
# 현재 폴더의 views를 import

urlpatterns = [
    path('', article_views.index, name="articles"),
    path('articles/<int:article_id>/edit/', article_views.edit, name="edit"),
    path('articles/<int:article_id>/delete/', article_views.delete, name="delete"),
    path('comments/', article_views.comments, name="comments"),
    path('comments/<int:comment_id>/delete/', article_views.delete_comment, name="delete_comment"), # 몇번 댓글인지
    path('comments/<int:comment_id>/edit/', article_views.edit_comment, name="edit_comment")
]
