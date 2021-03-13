from django.urls import path
from .views import home, products, customer, createOrders, updateOrder, deleteOrder, registerPage, loginPage, logoutUser

urlpatterns = [
    path('', home, name = 'home'),
    path('register', registerPage, name = 'register'),
    path('login', loginPage, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('products', products, name = 'products'),
    # <str:pk> передаем строковое занчение в pk
    path('customer/<str:pk>', customer, name = 'customer'),
    path('create_order/<str:pk>', createOrders, name = 'create_order'),
    path('update_order/<str:pk>', updateOrder, name = 'update_order'),
    path('delete_order/<str:pk>', deleteOrder, name = 'delete_order'),
]