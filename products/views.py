from django.shortcuts import render

# Create your views here.

def newProduct(request):
    return render(request, template_name="new-product.html")

def product(request, product_id):
    return render(request, template_name="product.html")

def wishList(request):
    return render(request, template_name="wishlist.html")