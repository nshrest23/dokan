from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "col-md-6 mb-4", "class": "form-control form-control-lg", "placeholder": "Enter First Name"}),
            "last_name": forms.TextInput(attrs={"class": "col-md-6 mb-4", "class": "form-control", "placeholder": "Enter Last Name"}),
            "username": forms.TextInput(attrs={"class": "col-md-6 mb-4", "class": "form-control", "placeholder": "Enter Username"}),
            "email": forms.EmailInput(attrs={"class": "col-md-6 mb-4", "class": "form-control", "placeholder": "Enter Email"}),
            "password": forms.PasswordInput(attrs={"class": "col-md-6 mb-4", "class": "form-control", "placeholder": "Enter Password"}),
        }
        help_texts = {
            'username': None,
        }
        labels = {
            "first_name": '', 
            "last_name": '',
            "username": ' ',
            "email": ' ',
            "password": ' ',
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Username"}),
            "password": forms.PasswordInput(attrs={"class": "form-control form-control-lg", "placeholder": "Enter Password"}),
        }
        help_texts = {
            'username': None,
        }
        labels = {
            "username": '',
            "password": '',
        }
