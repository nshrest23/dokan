from django.urls import path
import products.views as views

urlpatterns = [
    path("new_product", views.newProduct, name="newproduct_page"),
    path("product/<int:product_id>", views.product, name="product_page"),
    path("wishlist", views.wishList, name="wishlist_page"),
]
