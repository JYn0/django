from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('', views.index, name="index"), # main 페이지는 채팅 목록
    path('<int:room_id>/', views.show, name="room"), # 채팅방
    path('<int:room_id>/exit/', views.exit, name="exit"), # 채팅방 나가기
    path('<int:room_id>/message', views.chat, name="chat") 
]