from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('inicioS', views.inicioS, name='inicioS'),
    path('registros', views.registros, name='registros'),
]
