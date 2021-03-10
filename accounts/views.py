from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Customer, Pruduct, Order
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт успешно создан,' + user )
            return redirect('login')
    context = {'form': form}

    return render(request, 'accounts/register.html' ,context)

def loginPage(request):
    if request.method == 'POST':
        # Из запросв получаем логин и пароль
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Делаем аунтификацию
        user = authenticate(request, username = username, password = password)
        # Если пользователь существует в системе
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'accounts/login.html', context)

def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()
    # Общее количество клиентов
    total_customers = customer.count()
    # Общее количество заказов
    total_order = order.count()
    # Выбираем заказы с фильтром -доставлено
    delivered = order.filter(status = 'Доставлено').count()
    # Выбираем заказы с фильтром -в ожидании
    pending = order.filter(status = 'В ожидании').count()

    context = {'orders': order, 'customers': customer , 'total_customers': total_customers, 
               'total_order': total_order, 'delivered': delivered, 'pending': pending}
    
    return render(request, 'accounts/dashboard.html', context)
    
def products(request):
    # Выбрать из базы всю пролукцию
    products = Pruduct.objects.all()
    # {'pruducts':products} - передать в шаблон контекст для вывода
    return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk):
    # Получить пользователя по id
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    # Фильтр заказа, request.GET - запрос от формы, queryset - набор полей из формы
    myFilter = OrderFilter(request.GET, queryset = orders)
    # Переопределяем заказы (orders) с параметрами из поиска (myFilter.qs)
    orders = myFilter.qs
    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count,
                'myfilter': myFilter}
    return render(request, 'accounts/customer.html', context)

def createOrders(request, pk):
    # inlineformset_factory - объединение моделей в форме Customer (родительский объект) Order (дочерний объект)
    # fields - разрешение полей для Order (заказа) - продукция и статус
    # extra - вывд 10 строк на форме
    OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra= 10)
    customer = Customer.objects.get(id = pk)
    # Форма с набором OrderFormSet, instance - ссылается на объект customer
    formset = OrderFormSet(queryset = Order.objects.none(), instance = customer)
    # Создание заказа 
    #form = OrderForm(initial = {'customer':customer})
    # При отправленной форме с данными
    if request.method == 'POST':
        #print (request.POST)
        # создаем новую форму с заполненными данными
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance = customer)
        if formset.is_valid:
            formset.save()
            return redirect ('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    # Обновление заказа
    order = Order.objects.get(id = pk)
    form = OrderForm(instance = order)

    if request.method == 'POST':
        #print (request.POST)
        # создаем новую форму с заполненными данными
        form = OrderForm(request.POST, instance = order)
        if form.is_valid:
            form.save()
            return redirect ('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    # Удаление товара
    order = Order.objects.get(id = pk)
    # Если пришла заполненная форма на удаление
    if request.method == 'POST':
        # Удаление заказа
        order.delete()
        # Перенаправдяем на домашнюю страницу
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete_order.html', context)
