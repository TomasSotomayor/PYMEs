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
    
    
class GRUPO2(models.Model):
    id_grupo = models.AutoField(primary_key=True)  # Identificador autoincrementable
    name = models.CharField(max_length=100)  # Nombre del grupo, obligatorio

    def __str__(self):
        return self.name  # Retorna el nombre del grupo

class UserGrupo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con la tabla User
    grupo = models.ForeignKey(GRUPO2, on_delete=models.SET_NULL, null=True, blank=True)  # Grupo al que pertenece el usuario, puede ser nulo

    def __str__(self):
        return f"{self.user.username} - {self.grupo.name if self.grupo else 'No pertenece a un grupo'}"  # Retorna la cadena con el nombre del usuario y el grupo
