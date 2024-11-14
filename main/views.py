from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomLoginForm, CustomUserCrearionForm, PYMEForm,PYMEForm2
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import PYME,UserGrupo


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

def vistaAdmin(request):
    return render(request, 'main/vistaAdmin.html')

def pyme_usuario(request):
    pymes = PYME.objects.filter(user=request.user)
    # Verifica los IDs de todas las pymes
    for pyme in pymes:
        print(f"PYME ID: {pyme.id_PYME}, Nombre: {pyme.nombre}")  # Verifica los IDs de las pymes
    
    context = {'pymes': pymes}
    return render(request, 'main/pyme_usuario.html', context)


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

# funciones crud_admin


def user_list(request):
    group = Group.objects.get(id=2)  # Obtén el grupo con ID 2
    users = group.user_set.all()  # Obtén todos los usuarios en ese grupo
    return render(request, 'main/crud_admin/user_list.html', {'users': users})


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'main/crud_admin/user_detail.html', {'user': user})

def user_create(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(id=2)  # Asigna el grupo con ID 2
            user.groups.add(group)
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'main/crud_admin/user_form.html', {'form': form})

def user_update(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'main/crud_admin/user_form.html', {'form': form})

def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'main/crud_admin/user_confirm_delete.html', {'user': user})

#crud pyme


def pyme_list(request):
    pymes = PYME.objects.all()
    return render(request, 'main/crud_pyme/pyme_list.html', {'pymes': pymes})

def pyme_detail(request, id):
    pyme = get_object_or_404(PYME, id_PYME=id)
    return render(request, 'main/crud_pyme/pyme_detail.html', {'pyme': pyme})


def pyme_create(request):
    if request.method == "POST":
        form = PYMEForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pyme_list')
    else:
        form = PYMEForm()
    return render(request, 'main/crud_pyme/pyme_form.html', {'form': form})

def pyme_update(request, id):
    pyme = get_object_or_404(PYME, id_PYME=id)
    if request.method == "POST":
        form = PYMEForm(request.POST, instance=pyme)
        if form.is_valid():
            form.save()
            return redirect('pyme_list')
    else:
        form = PYMEForm(instance=pyme)
    return render(request, 'main/crud_pyme/pyme_form.html', {'form': form})

def pyme_delete(request, id):
    pyme = get_object_or_404(PYME, id_PYME=id)
    if request.method == "POST":
        pyme.delete()
        return redirect('pyme_list')
    return render(request, 'main/crud_pyme/pyme_confirm_delete.html', {'pyme': pyme})


#crud usuarios

def edit_pyme_usuario(request, pyme_id):
    pyme = get_object_or_404(PYME, pk=pyme_id)

    if request.method == 'POST':
        form = PYMEForm2(request.POST, request.FILES, instance=pyme)  # No olvides agregar request.FILES
        if form.is_valid():
            form.save()
            return redirect('pyme_usuario')
    else:
        form = PYMEForm2(instance=pyme)

    context = {'form': form, 'pyme': pyme}
    return render(request, 'main/edit_pyme_usuario.html', context)

def pyme_delete_usuario(request, pyme_id):
    pyme = get_object_or_404(PYME, pk=pyme_id)  # Obtener la PYME por ID

    if request.method == 'POST':  # Confirmación de eliminación
        pyme.delete()  # Eliminar el objeto PYME de la base de datos
        return redirect('pyme_usuario')  # Redirigir al listado de PYMES

    return render(request, 'main/confirmar_eliminar.html', {'pyme': pyme}) 

def pyme_create_user(request):
    if request.method == 'POST':
        form = PYMEForm2(request.POST, request.FILES)  # Asegúrate de manejar los archivos (imagen)
        if form.is_valid():
            form.save()  # Guardar la nueva PYME en la base de datos
            return redirect('pyme_usuario')  # Redirigir al listado de PYMES
    else:
        form = PYMEForm2()  # Formulario vacío

    return render(request, 'main/pyme_create_user.html', {'form': form})