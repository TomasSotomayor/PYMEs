from django.db import models
from django.contrib.auth.models import User  # Modelo User de auth_user

class PYME(models.Model):
    id_PYME = models.AutoField(primary_key=True)  # autoincrementable
    nombre = models.CharField(max_length=20)  # obligatoria
    direccion = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey('CATEGORIA', on_delete=models.SET_NULL, null=True)  # Clave foránea a CATEGORIA
    descripcion = models.CharField(max_length=500)  # obligatoria
    estado = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # clave foránea conectada con User

    def __str__(self):
        return self.nombre


class RESENNA(models.Model):
    puntuacion = models.IntegerField()  # obligatoria
    comentario = models.CharField(max_length=500, blank=True, null=True)
    pyme = models.ForeignKey(PYME, on_delete=models.CASCADE)  # clave foránea conectada con PYME

class REPORTE(models.Model):
    id_reporte = models.AutoField(primary_key=True)  # autoincrementable
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    pyme = models.ForeignKey(PYME, on_delete=models.CASCADE)  # clave foránea conectada con PYME

class CATEGORIA(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20) 

    def __str__(self):
        return self.nombre