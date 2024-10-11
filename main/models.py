from django.db import models

# Create your models here.

class Usuario(models.Model):
    run = models.PositiveIntegerField(primary_key=True)
    dv_run = models.CharField(max_length=1)
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20)
    ap_paterno = models.CharField(max_length=20)
    ap_materno = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=20)
    moderador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.p_nombre} {self.ap_paterno}"

class Pyme(models.Model):
    id_PYME = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=500)
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Resenna(models.Model):
    puntuacion = models.PositiveSmallIntegerField()
    comentario = models.CharField(max_length=500, blank=True, null=True)
    pyme = models.ForeignKey(Pyme, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reseña {self.puntuacion} para {self.pyme.nombre}"

class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    pyme = models.ForeignKey(Pyme, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reporte {self.id_reporte} para {self.pyme.nombre}"
