from django.contrib import admin
from django.urls import path, include
from .views import *
from .api_views import ModelApiList
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
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name="password_reset_complete"),
    path('katalog', katalog, name='katalog'),
    path('api/models', ModelApiList.as_view()),
    path('cars/add', create, name='create'),
    path('cars/<int:id>', get_car_by_id, name='get_car_by_id'),

]