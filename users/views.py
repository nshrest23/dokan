from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from users.models import User, Profile
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, template_name="index.html")

def user_login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form_data = UserLoginForm(request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data["username"]
            password = form_data.cleaned_data["password"]
            #username = request.POST.get("email")
            #password = request.POST.get("password")
            check_user = User.objects.filter(username=username)
            if not check_user.exists:
                error = "User doesnot exists!"
                messages.error(request, error)
                return redirect("/login")
            valid_user = authenticate(request, username=check_user[0].username, password=password)
            if valid_user:
                login(request, valid_user)
                return redirect("/profile")
            else:
                error = "Invalid Credentials!"
                messages.error(request, error)
                return redirect("/login")
    return render(request, "login.html", {"form": form})

def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form_data = UserRegisterForm(request.POST)
        if form_data.is_valid():
            #print("Form Data: ", form_data.cleaned_data)
            password = form_data.cleaned_data["password"]
            confirm_password = form_data.cleaned_data["confirm_password"]
            if password != confirm_password:
                error = "Password and Confirm Password fields does not match"
                messages.error(request, error)
                return redirect("/register")
            check_user = User.objects.filter(username=form_data.cleaned_data["username"]).exists()
            check_email = User.objects.filter(email=form_data.cleaned_data["email"]).exists()
            if check_user or check_email:
                error = "Username or Email already exists"
                messages.error(request, error)
                return redirect("/register")
            user_account_data = {
                "first_name": form_data.cleaned_data["first_name"],
                "last_name": form_data.cleaned_data["last_name"],
                "username": form_data.cleaned_data["username"],
                "email": form_data.cleaned_data["email"],
            }
            user = User.objects.create(**user_account_data)
            user.set_password(password)
            user.save()
            profile_data = {
                "user": user,
                "phone": form_data.cleaned_data["phone"],
                "address": form_data.cleaned_data["address"],
                "city": form_data.cleaned_data["city"],
                "profile_pic": "N/A",
            }
            
            profile = Profile.objects.create(**profile_data)
        return redirect("/login")
    
    return render(request, "register.html", {"form": form})

@login_required
def user_profile(request):
    uid = request.user.pk
    profile = Profile.objects.get(user_id=uid)
    context = {"profile": profile}
    return render(request, "profile.html", context)

@login_required
def editprofile(request):
    uid = request.user.pk
    profile = Profile.objects.get(user_id=uid)
    context = {"profile": profile}
    return render(request, "edit-profile.html", context)

def user_logout(request):
    logout(request)
    return redirect("/login")

