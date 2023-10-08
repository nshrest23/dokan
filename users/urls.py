from django.urls import path
import users.views as views

urlpatterns = [
    path("", views.Home, name="homepage"),
]
