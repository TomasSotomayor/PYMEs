from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def inicioS(request):
    return render(request, 'main/inicioS.html')

def registros(request):
    return render(request, 'main/registros.html')