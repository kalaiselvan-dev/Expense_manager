from django import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home_page"),
    path('home/', home1, name="home"),
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('update/', update, name="update"),
    path('delete/', delete, name="delete"),
    # path('edit/', edit, name="edit")
]
