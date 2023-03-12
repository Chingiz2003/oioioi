from django.contrib import admin
from django.urls import path, include
from .views import *
from django.http import HttpResponse
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registr/', registr, name='registr'),
    path('success/', success, name='success'),
    path('', index, name='home'),
    path('index/', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('proba/', proba, name='proba'),
    path('create/', create, name='create'),
    path('news_home/', news_home, name='news_home'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name="password_reset_complete"),
]