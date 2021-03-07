from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Загрузка модели пользователя
from django.contrib.auth.models import User
from .models import Order


class OrderForm(ModelForm):
    # Форма индивидуального заказа
    class Meta:
        model = Order
        # Разрешение полей модели Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']