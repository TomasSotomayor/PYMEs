from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import productos

urlpatterns = [
    path('index/', views.index, name='index'),
    path('inicioS', views.inicioS, name='inicioS'),
    path('registros', views.registros, name='registros'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('productos/', views.productos, name='productos'),
    path('pymebase/', views.pymebase, name='pymebase'),
    # Otras rutas...
]
