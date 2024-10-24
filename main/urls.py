from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import productos

urlpatterns = [
    path('index/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('pymebase/', views.pymebase, name='pymebase'),
    path('servicios/', views.servicios, name='servicios'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/',views.registro, name='registro' ),
    
]
