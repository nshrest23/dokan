from django.urls import path
import orders.views as views

urlpatterns = [
    path("cart", views.Cart, name="cart_page"),
    path("checkout", views.Checkout, name="checkout_page"),
    path("order", views.Order, name="order_page"),
]
