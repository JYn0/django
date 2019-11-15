"""crudtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# url 분리하기

# from boards import views as boards_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls'))
    # # 게시판의 메인페이지, 전체 리스트 페이지
    # path('boards/', boards_views.index),
    # # 게시판의 새 글을 작성하는 페이지
    # path('boards/new/', boards_views.new),
    # path('boards/create/', boards_views.create),
    # # 게시판의 글 하나를 상세히 보는 페이지
    # path('boards/<id>/', boards_views.show)
]
