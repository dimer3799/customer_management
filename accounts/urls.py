from django.urls import path
from .views import home, products, customer

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    # <str:pk> передаем строковое занчение в pk
    path('customer/<str:pk>', customer, name='customer'),
]