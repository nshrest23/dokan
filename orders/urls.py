from django.urls import path
import orders.views as views

urlpatterns = [
    path("cart", views.cart, name="cart_page"),
    path("checkout", views.checkout, name="checkout_page"),
    path("order", views.order, name="order_page"),
]
