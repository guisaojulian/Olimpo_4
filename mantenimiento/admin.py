from mantenimiento.models import CorrectivoModel, ElementoModel, OtModel, PreventivoModel, SistemaModel
from django.contrib import admin

# Register your models here.
admin.site.register(SistemaModel)
admin.site.register(ElementoModel)
admin.site.register(PreventivoModel)
admin.site.register(CorrectivoModel)
admin.site.register(OtModel)