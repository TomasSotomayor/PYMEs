from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import productos
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('index/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('pymebase/', views.pymebase, name='pymebase'),
    path('servicios/', views.servicios, name='servicios'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/',views.registro, name='registro' ),
    path('vistaAdmin/',views.vistaAdmin, name='vistaAdmin'),
    path('vista_moderador',views.vista_moderador, name='vista_moderador'),
    path('lista_reportes',views.lista_reportes, name='lista_reportes'),

    #urls crud_admin
    path('users/', views.user_list, name='user_list'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:id>/update/', views.user_update, name='user_update'),
    path('users/<int:id>/delete/', views.user_delete, name='user_delete'),

    #urls crud_pyme
    path('pymes/', views.pyme_list, name='pyme_list'), 
    path('pymes/<int:id>/', views.pyme_detail, name='pyme_detail'), 
    path('pymes/create/', views.pyme_create, name='pyme_create'), 
    path('pymes/<int:id>/update/', views.pyme_update, name='pyme_update'), 
    path('pymes/<int:id>/delete/', views.pyme_delete, name='pyme_delete'),

    #urls usuarios
    path('pyme_usuario/',views.pyme_usuario, name='pyme_usuario'),
    path('pyme_usuario/edit/<int:id_pyme>/', views.pyme_usuario_edit, name='pyme_usuario_edit'),
    path('pyme_usuario/delete/<int:id_pyme>/', views.pyme_usuario_delete, name='pyme_usuario_delete'),
    path('pyme/<int:id_PYME>/', views.pyme, name='pyme'),
    path('pyme/<int:id_PYME>/reportar/', views.report_pyme, name='report_pyme'),
    path('reportes/', views.listar_reportes, name='listar_reportes'),
    path('reporte/<int:reporte_id>/delete/', views.reporte_delete, name='reporte_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)