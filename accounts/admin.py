from django.contrib import admin

# Register your models here.
from .models import Customer, Pruduct, Order, Tag

admin.site.register(Customer)
admin.site.register(Pruduct)
admin.site.register(Tag)
admin.site.register(Order)