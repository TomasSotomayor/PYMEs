from django.contrib import admin
from .models import PYME, RESENNA, REPORTE

# Registra los modelos en el admin
admin.site.register(PYME)
admin.site.register(RESENNA)
admin.site.register(REPORTE)
