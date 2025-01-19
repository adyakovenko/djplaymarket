from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import UserRegister
from .models import *


games = ['Ветер', 'Лучик', 'Красный цвет']
games = Game.objects.values_list('title', 'description', 'cost')
text_title = 'Главная страница'
text_apologies = 'Простите, мы не умеем продавать'
text_button_buy = 'Купить'
text_button_back = 'На главную'

context = {
    'text_title': text_title,
    'games': games,
    'text_apologies': text_apologies,
    'text_button_buy': text_button_buy,
    'text_button_back': text_button_back
}


def market(request):
    template_name = 'market.html'
    local_context = context
    local_context['title'] = 'Магазин'
    return render(request, template_name, local_context)


def cart(request):
    template_name = 'cart.html'
    local_context = context
    local_context['title'] = 'Корзина'
    return render(request, template_name, local_context)


def menu(request):
    return render(request, 'menu.html', context)


def sign_up_by_django(request):
    if request.method == 'POST':
        buyers = [val[0] for val in Buyer.objects.values_list('name')]
        form = UserRegister(request.POST)
        name = form.data['username']
        password = form.data['password']
        password_repeat = form.data['repeat_password']
        age = form.data['age']
        flag = True
        error = ''

        if password_repeat != password:
            flag = False
            error = 'Пароли не совпадают'
        if int(age) < 18:
            flag = False
            error = 'Вы должны быть старше 18'
        if name in buyers:
            flag = False
            error = "Пользователь уже существует"
        info = {'form': form, 'error': error}
        if flag:
            return HttpResponse(f"Добро пожаловать, {name}")
        else:
            Buyer.objects.create(name = name, balance=0, age=age)
            return render(request, 'user.html', info)
    else:
        form = UserRegister()
    return render(request, 'user.html', {'form': form})


def sign_up_by_html(request):
    if request.method == 'POST':
        buyers = [val[0] for val in Buyer.objects.values_list('name')]
        name = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('repeat_password')
        age = request.POST.get('age')
        flag = True
        error = ''

        if password_repeat != password:
            flag = False
            error = 'Пароли не совпадают'
        if int(age) < 18:
            flag = False
            error = 'Вы должны быть старше 18'
        if name in buyers:
            flag = False
            error = "Пользователь уже существует"
        if flag:
            Buyer.objects.create(name=name, balance=0, age=age)
            return HttpResponse(f"Добро пожаловать, {name}")
        else:
            info = {'error': error}
            return render(request, 'user.html', info)

    return render(request, 'user.html')


def news(request):
    news = News.objects.all().order_by('date')
    paginator = Paginator(news, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_obj})