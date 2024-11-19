# main/forms.py

from django import forms
from .models import PYME
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))

class CustomUserCrearionForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username',"first_name","last_name", "email","password1", "password2" ]


class PYMEForm(forms.ModelForm):
    class Meta:
        model = PYME
        fields = ['nombre', 'direccion', 'categoria', 'descripcion', 'estado', 'user']

class PYMEForm2(forms.ModelForm):
    class Meta:
        model = PYME
        fields = ['nombre', 'direccion', 'categoria', 'descripcion', 'estado', 'imagen']
