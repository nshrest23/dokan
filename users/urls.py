from django.urls import path
import users.views as views

urlpatterns = [
    path("", views.Home, name="home_page"),
    path("login", views.Login, name="login_page"),
    path("register", views.Register, name="register_page"),
    path("profile", views.Profile, name="profile_page"),
]
