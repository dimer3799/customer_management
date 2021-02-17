from django.urls import path
from .views import home, products, customer, createOrders, updateOrder

urlpatterns = [
    path('', home, name = 'home'),
    path('products', products, name = 'products'),
    # <str:pk> передаем строковое занчение в pk
    path('customer/<str:pk>', customer, name = 'customer'),
    path('create_order/', createOrders, name = 'create_order'),
    path('update_order/<str:pk>', updateOrder, name = 'update_order'),
]