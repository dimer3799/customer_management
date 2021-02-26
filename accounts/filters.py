import django_filters
from django_filters import DateFilter, CharFilter
from .models import Order

class OrderFilter(django_filters.FilterSet):
    ''' Класс фильтрации для поиска'''

    # Настройка своих полей
    # field_name - имя поля
    # lookup_expr - параметры поиска (gte - больше или равно, lte - меньше или равно)
    start_date = DateFilter(field_name = 'date_created', lookup_expr = 'gte')
    end_date = DateFilter(field_name = 'date_created', lookup_expr = 'lte')
    # lookup_expr = 'icontains' игнорировать регистр
    note = CharFilter(field_name = 'note', lookup_expr = 'icontains')
    class Meta:
        # model - на основе какокой модели
        model = Order
        # fields - какие поля взять
        fields = '__all__'
        # exclude - исключающие поля
        exclude = ['customer', 'date_created']