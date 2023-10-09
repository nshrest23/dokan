from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prooduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    delivery_status = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)  

class OrderSummary(models.Model):
    subtotal = Order.total
    reciept_voucher = models.CharField()
    invoice_number = models.IntegerField()
    invoice_date = models.DateField(auto_now_add=True)
    discount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    delivery_charge = models.FloatField(default=0)
    total_amount = models.FloatField(default=0)
    

def __str__(self):
    return self.total
