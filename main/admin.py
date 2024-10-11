from django.contrib import admin
from .models import Usuario, Pyme, Resenna, Reporte
# Register your models here.


# Registra los modelos en el administrador
admin.site.register(Usuario)
admin.site.register(Pyme)
admin.site.register(Resenna)
admin.site.register(Reporte)
