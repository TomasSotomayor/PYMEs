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
    path('vistaAdmin/',views.vistaAdmin, name='vistaAdmin'),

    #urls crud_admin
    path('users/', views.user_list, name='user_list'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:id>/update/', views.user_update, name='user_update'),
    path('users/<int:id>/delete/', views.user_delete, name='user_delete'),
]
