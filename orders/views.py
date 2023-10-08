from django.shortcuts import render

# Create your views here.

def Cart(request):
    return render(request, template_name="cart.html")

def Checkout(request):
    return render(request, template_name="checkout.html")

def Order(request):
    return render(request, template_name="order.html")
