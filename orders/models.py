from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'cart'



class Order(models.Model):
    order_status = [ ("PENDING", "PENDING"), ("ON_TRACK", "ON_TRACK"), ("DELIVERED", "DELIVERED"), ("CANCELLED", "CANCELLED")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.JSONField()
    total = models.FloatField(default=0)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    info = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50, default="Cash on Delivery")
    status = models.CharField(max_length=20, choices=order_status, default="PENDING") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'order'
    
    def __str__(self):
     return self.id
