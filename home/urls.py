from django.urls import path, include

from home.views import *

urlpatterns = [
    path('', home, name="home"),
]
