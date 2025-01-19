from django import forms


class UserRegister(forms.Form):
    name = forms.CharField(max_length=30, label='Ваше имя')
    password = forms.CharField(min_length=8, label='Пароль')
    password_repeat = forms.CharField(min_length=8, label='Повторение пароля')
    age = forms.CharField(max_length=3, label='Возраст')
