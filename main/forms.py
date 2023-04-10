from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, EmailField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
# from .models import Ads
# from django.forms import ModelForm, TextInput, DateTimeInput


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User 
		fields = ('username', 'email', 'password1', 'password2')


# class AdsForm(ModelForm):
# 	class Meta:
# 		model = Ads
# 		fields = ['brand', 'mode', 'year', 'dvig', 'mileage', 'rule', 'full_text', 'date']

# 		widgets = {
# 			"brand": TextInput(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Введите марку'
# 			}),
# 			"mode": TextInput(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Введите модель'
# 			}),
# 			"year": TextInput(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Год выпуска'
# 			}),
# 			"dvig": TextInput(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Тип двигателя'
# 			}),
# 			"mileage": TextInput(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Пробег'
# 			}),
# 			"rule": TextInput(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Расположение руля'
# 			}),
# 			"full_text": Textarea(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Описание'
# 			}),
# 			"date": DateTimeInput(attrs={
# 				'class': 'form-control',
# 				'placeholder': 'Дата'
# 			})
# 		}

class AdsCreateForm(ModelForm):
	class Meta: 
		model = Ads
		fields = ('category', 'marks', 'mark_model', 'year', 'engine', 'mileage', 'rudder', 'full_text', 'photo', 'price')