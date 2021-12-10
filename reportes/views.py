from django.views.generic import TemplateView
from .forms import *

# Create your views here.

class Reportes(TemplateView):
    template_name = 'reportes/reporte.html'
    def enviar_datos_reporte(self, **kwargs):
        context = super().enviar_datos_reporte(**kwargs)
        context['title'] = 'Reporte de las ventas'
        context['form'] = ReporteForms()
        return context 
