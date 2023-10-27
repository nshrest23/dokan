from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'category'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    product_img = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'product'
    
    def __str__(self):
        return self.title