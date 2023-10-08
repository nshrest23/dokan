from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, template_name="index.html")

def Login(request):
    return render(request, template_name="login.html")

def Register(request):
    return render(request, template_name="register.html")

def Profile(request):
    return render(request, template_name="profile.html")
