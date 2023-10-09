from django.urls import path
import products.views as views

urlpatterns = [
    path("new_product", views.NewProduct, name="newproduct_page"),
    path("product/<int:product_id>", views.Product, name="product_page"),
    path("wishlist", views.WishList, name="wishlist_page"),
]
