from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from orders.models import Cart, Order
from products.models import Product
from django.conf import settings
import string 
import random

# Create your views here.

@login_required
def cart(request):
    carts = Cart.objects.filter(user=request.user).order_by("-created_at")
    has_item = len(carts) > 0
    total_cart_amount = 0
    grand_total = 0
    vat_amount = 0
    if has_item:
        total_cart_amount = sum([cart.total for cart in carts])
        vat_amount = total_cart_amount * 0.13
        grand_total = total_cart_amount + vat_amount

    context = { "carts": carts, "has_item": has_item, "total_cart_amount": total_cart_amount, "vat_amount": vat_amount, "grand_total": grand_total }
    return render(request, "cart.html", context)

@login_required
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_data = {
        "user": request.user,
        "product": product,
        "quantity": 1,
        "total": product.price,
    }
    check_cart = Cart.objects.filter(user_id=request.user.pk, product_id=product_id)
    if check_cart.exists():
        cart = check_cart.first()
        cart.quantity = cart.quantity + 1
        cart.total = cart.quantity * product.price
        if product.quantity >= cart.quantity:
            cart.save()
    else:
        Cart.objects.create(**cart_data)
    return redirect("/")

@login_required
def update_cart(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    if request.method == "POST":
        qty = request.POST.get("qty")
        cart.quantity = qty
        cart.total = int(qty) * cart.product.price
        if int(cart.quantity) >= int(qty):
            cart.save()           
    return redirect("/cart")

@login_required
def delete_cart(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    cart.delete()
    return redirect("/cart")

@login_required
def checkout(request):
    carts = Cart.objects.filter(user=request.user.pk)
    cart_total = sum([cart.total for cart in carts])

    context = {"carts": carts, "cart_total": cart_total }
    
    if request.method == "POST":
        shipping_type = request.POST.get("shipping_type")
        info = request.POST.get("info")
        address = request.POST.get("address")
        city = request.POST.get("city")
        coupon = request.POST.get("coupon")
        vat_amount = cart_total * 0.13
        shipping_cost = float(settings.SHIPPING_CHARGE[shipping_type])
        if coupon in settings.COUPON_CODE:
            discount = float(settings.COUPON_CODE[coupon])
        else:
            discount = 0
        grand_total = cart_total + vat_amount + shipping_cost - discount
        order_details = {
            "user_id": request.user.pk,
            "products": [{
                "product_id": cart.product.pk,
                "title": cart.product.title,
                "category": cart.product.category.name,
                "product_img": cart.product.product_img,
                "product_qty": cart.quantity,
                "product_price": cart.product.price,
                "total": cart.quantity * cart.product.price,
            }for cart in carts],
            "info": info,
            "address": address,
            "city": city,
            "cart_total": cart_total,
            "discount": discount,
            "vat_amount": vat_amount,
            "shipping_type": shipping_type,
            "shipping_cost": shipping_cost,
            "grand_total": grand_total,
        }
        request.session["order_details"] = order_details
        return redirect("/purchase")
    return render(request, "checkout.html", context)

@login_required
def purchase(request):
    order_details = request.session.get("order_details")
    context = {"order_details": order_details}
    # generating invoice_id random strings
    invoice_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    if request.method == "POST":
        # save order
        order_details = {
            "user_id": request.user.pk,
            "invoice_id": invoice_id,
            "products": request.session["order_details"]["products"],
            "info": request.session["order_details"]["info"],
            "address": request.session["order_details"]["address"],
            "city": request.session["order_details"]["city"],
            "total": request.session["order_details"]["cart_total"],
            "discount": request.session["order_details"]["discount"],
            "vat_amount": request.session["order_details"]["vat_amount"],
            "shipping_type": request.session["order_details"]["shipping_type"],
            "shipping_cost": request.session["order_details"]["shipping_cost"],
            "grand_total": request.session["order_details"]["grand_total"],
            "payment_method": "COD",
            "status": "processing",
        }
        Order.objects.create(**order_details)
        # update products inventory
        products = request.session["order_details"]["products"]
        for p in products:
            product = Product.objects.get(id=p["product_id"])
            qty = product.quantity
            product.quantity = qty - p["product_qty"]
            product.save()

        # delete cart & delete session
        Cart.objects.filter(user_id=request.user.pk).delete()
        del request.session["order_details"]
        print("Purchase Complete!",order_details)
        return redirect("/thanks")

    return render(request, "purchase.html", context)

@login_required
def order(request):
    orders = Order.objects.filter(user_id=request.user.pk).order_by("-created_at")
    has_order = len(orders) > 0
    if orders.exists():
        ordered_products = []
        created_at = None
        status_code = 0
        for o in orders:
            product = o.products
            ordered_products.extend(product)
            total = o.total
            created_at = o.created_at           
            status = o.status
            if status == "processing":
                status_code = 25
            elif status == "shipped":
                status_code = 50
            elif status == "out_for_delivery":
                status_code = 75
            elif status == "delivered":
                status_code = 100
            elif status == "cancelled":
                status_code = 0
            
    context = {"orders": orders, "has_order": has_order}   
    return render(request, "order.html", context)


@login_required
def thanks(request):
    return render(request, "thankyou.html")

@login_required
def invoice(request):
    return render(request, "invoice.html")
