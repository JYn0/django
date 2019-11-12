"""day5 URL Configuration

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
from django.urls import path

# 위치가 달라서 import 해줘야 함
# view 이름 겹치지 않게 as 사용할이름
from lotto import views as lotto_views
from ascii import views as ascii_views
from opgg import views as opgg_views

# app.route에 붙었던 것들 써주기
urlpatterns = [
    # path(어떤 주소로 받을지, 어떤 함수를 실행할지)
    path('admin/', admin.site.urls),
    path('lotto/', lotto_views.lotto), 
    path('lotto/winning/', lotto_views.winning),
    path('ascii/', ascii_views.ascii),
    path('ascii/result/', ascii_views.result),
    path('opgg/', opgg_views.opgg),
    path('opgg/result', opgg_views.result)
]
