from django.urls import path
from .views import *


urlpatterns = [
    path('reporte/', Reportes.as_view(), name='reporte')


]