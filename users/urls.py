from django.urls import path
import users.views as views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("login", views.login, name="login_page"),
    path("register", views.register, name="register_page"),
    path("profile", views.profile, name="profile_page"),
    path("edit-profile", views.editprofile, name="editprofile_page")
]
