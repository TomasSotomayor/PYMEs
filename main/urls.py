from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('pymebase/', views.pymebase, name='pymebase'),
    path('servicios/', views.servicios, name='servicios'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('vistaAdmin/', views.vistaAdmin, name='vistaAdmin'),

    # urls CRUD usuarios
    path('users/', views.user_list, name='user_list'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:id>/update/', views.user_update, name='user_update'),
    path('users/<int:id>/delete/', views.user_delete, name='user_delete'),

    # urls CRUD pyme
    path('pymes/', views.pyme_list, name='pyme_list'),
    path('pymes/<int:id>/', views.pyme_detail, name='pyme_detail'),
    path('pymes/create/', views.pyme_create, name='pyme_create'),
    path('pymes/<int:id>/update/', views.pyme_update, name='pyme_update'),
    path('pymes/<int:id>/delete/', views.pyme_delete, name='pyme_delete'),

    # urls para pyme del usuario
    path('pyme_usuario/', views.pyme_usuario, name='pyme_usuario'),
    path('edit_pyme_usuario/<int:pyme_id>/', views.edit_pyme_usuario, name='edit_pyme_usuario'),
    path('pyme/<int:pyme_id>/delete/', views.pyme_delete_usuario, name='pyme_delete_usuario'),
    path('pyme/create/', views.pyme_create_user, name='pyme_create_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
