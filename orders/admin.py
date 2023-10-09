from django.contrib import admin
from orders.models import Cart, Order, OrderSummary

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderSummary)