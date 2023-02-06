from django.contrib import admin
from django.urls import path, include
from main import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('index', views.index),
    path('registr', views.registr),
]