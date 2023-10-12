from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def cart(request):
    return render(request, template_name="cart.html")

def checkout(request):
    return render(request, template_name="checkout.html")

#@login_required
def order(request):
    return render(request, template_name="order.html")
