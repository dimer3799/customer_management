from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    # Форма индивидуального заказа
    class Meta:
        model = Order
        # Разрешение полей модели Order
        fields = '__all__'