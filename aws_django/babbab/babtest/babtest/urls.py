"""babtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from babapp import views


urlpatterns = [
    path('', views.index),      #inmagobab.ml/로 접속했을 때 views.py파일의 index함수를 실행함
    path('admin/', admin.site.urls),    #inmagobab.ml/admin으로 접속했을 때 Django 관리 모드를 실행함
    path('keyboard/', views.keyboard),  #inmagobab.ml/keyboard로 접속했을 때 views.py파일의 keyboard함수를 실행함(카카오톡 api에 이용)
    path('message', views.message),     #카카오톡 사용자의 버튼 입력을 받으면 inmagobab.ml/message로 접속이 되는데 이때 views.py파일의 message함수를 실행
    path('info', views.info),    #inmagobab.ml/info로 접속하면 정보 페이지를 띄워주는 info함수를 실행함
    path('month', views.month),
    path('source', views.source),
]
