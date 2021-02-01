from django.db import models

# Create your models here.

class Customer(models.Model):
    # Клиенты
    name = models.CharField(max_length=200, null = True, verbose_name = 'ФИО')
    phone = models.CharField(max_length=200, null = True, verbose_name = 'Телефон')
    email = models.CharField(max_length=200, null = True, verbose_name = 'Эл. почта')
    date_created = models.DateTimeField(auto_now_add=True, null = True, verbose_name = 'Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'

class Pruduct(models.Model):
    # Продукция
    CATEGORY = (
        ('Для дома', 'Для дома'),
        ('Для улицы', 'Для улицы'),
    )
    name = models.CharField(max_length=200, null = True, verbose_name = 'Наименования')
    price = models.FloatField(null = True, verbose_name = 'Цена')
    category = models.CharField(max_length=200, null = True, choices = CATEGORY, verbose_name = 'Категория')
    description = models.CharField(max_length=200, null = True, verbose_name = 'Описание')
    date_created = models.DateTimeField(auto_now_add=True, null = True, verbose_name = 'Дата')

    class Meta:
        verbose_name_plural = 'Продукция'
        verbose_name = 'Продукция'

class Order(models.Model):
    #Заказы
    STATUS = (
        ('В ожидании', 'В ожидании'),
        ('Готово к доставке', 'Готово к доставке'),
        ('Доставлено', 'Доставлено'),
    )
    # customer = 
    # product = 
    date_created = models.DateTimeField(auto_now_add=True, null = True, verbose_name = 'Дата')
    status = models.CharField(max_length = 200, null = True, choices = STATUS, verbose_name = 'Статус заказа')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
    