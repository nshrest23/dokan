from django.shortcuts import render
from users.forms import RegisterForm, LoginForm

# Create your views here.
def Home(request):
    return render(request, template_name="index.html")

def Login(request):
    return render(request, template_name="login.html", context={'form': LoginForm})

def Register(request):
    return render(request, template_name="register.html", context = {'form': RegisterForm})

def Profile(request):
    return render(request, template_name="profile.html")
