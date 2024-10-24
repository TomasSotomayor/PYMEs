from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomLoginForm, CustomUserCrearionForm
from django.contrib.auth.models import Group



def index(request):
    return render(request, 'main/index.html')

def inicioS(request):
    return render(request, 'main/inicioS.html')

def registros(request):
    return render(request, 'main/registros.html')

def pymebase(request):
    return render(request, 'main/pymebase.html')

def productos(request):
    return render(request, 'main/productos.html')

def servicios(request):
    return render(request, 'main/servicios.html')

#funcion inicio de sesion
def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige a la página que desees tras el inicio de sesión
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    else:
        form = CustomLoginForm()

    return render(request, 'main/login.html', {'form': form})

def registro(request):
    data = {
        'form': CustomUserCrearionForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCrearionForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.save()  # Guardamos el usuario
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            
            # Asignar el grupo automáticamente
            grupo = Group.objects.get(id=1)  # Obtenemos el grupo con id=1
            usuario.groups.add(grupo)  # Agregamos el usuario al grupo
            
            return redirect(to='index')
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)