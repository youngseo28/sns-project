"""sns_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #mainpage URL 연결하기 with 별명사용
    path('',views.showmain, name="showmain"),

    #firstpage URL 연결하기 with 별명사용
    path('firstpage/', views.showfirst, name="showfirst"),

    #secondpage URL 연결하기 with 별명사용
    path('secondpage/', views.showsecond, name="showsecond"),

    #thirdpage URL 연결하기 with 별명사용
    path('thirdpage/', views.showthird, name="showthird"),

    #fourthpage URL 연결하기 with 별명사용
    path('fourthpage/', views.showfourth, name="showfourth"),

    #path-converter 하나의 템플릿으로 여러 경우의 페이지를 띄울 수 있게 함
    path('<int:id>',views.detail, name="detail"),

    path('new/',views.new, name="new"),

    path('create/', views.create, name="create"),
]
