from django.shortcuts import render

# Create your views here.

def NewProduct(request):
    return render(request, template_name="new-product.html")

def ProductDetail(request, product_id):
    return render(request, template_name="product-detail.html")

def WishList(request):
    return render(request, template_name="wishlist.html")