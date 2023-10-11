from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, template_name="cart.html")

def checkout(request):
    return render(request, template_name="checkout.html")

def order(request):
    return render(request, template_name="order.html")
