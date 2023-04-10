from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, AdsCreateForm
from django.contrib.auth import login, logout
from .models import Ads
# from .forms import AdsForm



# Create your views here.
def index(request):
     return render(request, 'main/index.html')


def registr(request):
    form = UserRegisterForm() 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('success')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/registr.html', {"form": form})

def success(request):
    return render(request, 'main/success.html')

def proba(request):
    ads = Ads.objects.all()
    return render(request, 'main/proba.html', {'ads': ads})

def katalog(request):
    ads = Ads.objects.all()
    return render(request, 'main/katalog.html', {'ads': ads})

def get_car_by_id(request, id):
    detailed = Ads.objects.get(id=id)
    return render(request, 'main/get_car_by_id.html', context={'ads': detailed})



def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('index')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')

# def create(request):
#     # ads = Ads.objects.all()
#     # res = '<h1>Каталог авто</h1>'
#     # for item in ads:
#     #     res += f'<div>\n<p>{item.brand}</p>\n<p>{item.mode}</p>\n</div>\n<hr>\n'
#     # return HttpResponse(res)
#     return render(request, 'main/create.html')

def create(request):
    form = AdsCreateForm()
    if request.method == 'POST':
        form = AdsCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно добавили публикацию!')
            return redirect('success')
        else:
            messages.error(request, 'Заполните все поля')
    else:
        form = AdsCreateForm()
    return render(request, 'main/create.html', context={'form': form})

 

       



#     error = ''
#     if request.method == "POST":
#         form = AdsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else: 
#             error = 'Форма неверная'

#     form = AdsForm()

#     data = {
#         'form': form,
#         'error': error
#     }

#     return render(request, 'main/create.html', data)







