from django.shortcuts import render
from products.models import Product

# Create your views here.

def newProduct(request):
    products = Product.objects.all().order_by('-created_at')[:8]
    context = {"products": products}
    return render(request, "new-product.html", context)

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "product.html", context)

def wishList(request):
    return render(request, template_name="wishlist.html")