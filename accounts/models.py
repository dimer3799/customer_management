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


class Tag(models.Model):
    # Тег товара
    name = models.CharField(max_length=200, null = True, verbose_name = 'Тег товара')

    class Meta:
        verbose_name_plural = 'Теги товара'
        verbose_name = 'Тег товара'

    def __str__(self):
        return self.name


class Pruduct(models.Model):
    # Продукция
    CATEGORY = (
        ('Для дома', 'Для дома'),
        ('Для улицы', 'Для улицы'),
    )
    name = models.CharField(max_length=200, null = True, verbose_name = 'Наименования')
    price = models.FloatField(null = True, verbose_name = 'Цена')
    category = models.CharField(max_length=200, null = True, choices = CATEGORY, verbose_name = 'Категория')
    description = models.CharField(max_length=200, null = True, verbose_name = 'Описание', blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True, verbose_name = 'Дата')
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = 'Продукция'
        verbose_name = 'Продукция'

    def __str__(self):
        return self.name


class Order(models.Model):
    #Заказы
    STATUS = (
        ('В ожидании', 'В ожидании'),
        ('Готово к доставке', 'Готово к доставке'),
        ('Доставлено', 'Доставлено'),
    )
    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL, verbose_name = 'Клиент')
    product = models.ForeignKey(Pruduct, null = True, on_delete = models.SET_NULL, verbose_name = 'Товар')
    date_created = models.DateTimeField(auto_now_add=True, null = True, verbose_name = 'Дата')
    status = models.CharField(max_length = 200, null = True, choices = STATUS, verbose_name = 'Статус заказа')
    note = models.CharField(max_length = 10000, null = True)

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'

    def __str__(self):
        return self.product.name