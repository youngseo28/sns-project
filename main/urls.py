from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('firstpage/', showfirst, name="showfirst"),
    path('secondpage/', showsecond, name="showsecond"),
    path('thirdpage/', showthird, name="showthird"),
    path('fourthpage/', showfourth, name="showfourth"),
    path('<int:id>',detail, name="detail"),
    path('new/',new, name="new"),
    path('create/', create, name="create"),
    path('posts/', posts, name="posts"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]