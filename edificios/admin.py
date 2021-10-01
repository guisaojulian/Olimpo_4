from edificios.models import Edificio_Model, Presupuesto_Cuenta, Presupuesto_Rubro, Presupuesto_Cuenta, Propietario_Model, Visitante_Model
from django.contrib import admin

# Register your models here.

admin.site.register(Propietario_Model)
admin.site.register(Visitante_Model)
admin.site.register(Presupuesto_Cuenta)
admin.site.register(Presupuesto_Rubro)
admin.site.register(Edificio_Model)