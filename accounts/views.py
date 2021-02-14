from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Pruduct, Order

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
    context = {'customer': customer, 'orders': orders, 'orders_count': orders_count}
    return render(request, 'accounts/customer.html', context)

# Create your views here.
