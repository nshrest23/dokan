from django.urls import path
import orders.views as views

urlpatterns = [
    path("cart", views.cart, name="cart_page"),
    path("checkout", views.checkout, name="checkout_page"),
    path("order", views.order, name="order_page"),
    path("addcart/<int:product_id>", views.add_cart, name="addcart_page"),
    path("deletecart/<int:cart_id>", views.delete_cart, name="deletecart_page"),
    path("update_cart/<int:cart_id>/<int:qty>", views.update_cart, name="updatecart_page"),
]
