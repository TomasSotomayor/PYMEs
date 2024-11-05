from django.contrib import admin
from .models import PYME, RESENNA, REPORTE, CATEGORIA

# Registra los modelos en el admin
admin.site.register(PYME)
admin.site.register(RESENNA)
admin.site.register(REPORTE)
admin.site.register(CATEGORIA)