# main/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))
