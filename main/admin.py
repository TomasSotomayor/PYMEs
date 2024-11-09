from django.contrib import admin
from .models import PYME, RESENNA, REPORTE, CATEGORIA, GRUPO2, UserGrupo

# Registra los modelos en el admin
admin.site.register(PYME)
admin.site.register(RESENNA)
admin.site.register(REPORTE)
admin.site.register(CATEGORIA)
admin.site.register(GRUPO2)
admin.site.register(UserGrupo)