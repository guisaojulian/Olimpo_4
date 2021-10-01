from os import name
from django.urls.resolvers import URLPattern
from django.urls import path
from django.contrib.auth.views import LoginView


#self
from .views import*
from . import views

urlpatterns = [
    path ('', views.ingresar, name='login'),
    
    path ('registro-edificios/', views.registro_edificios, name='registro_edificios'),
    path ('registro-personas/', views.registro_personas, name='registro_personas'),
    path ('registro-visitantes/', views.registro_visitantes, name='registro_visitantes'),
    path ('presupuesto-cuenta/', views.presupuesto_cuenta,name='presupuesto_cuenta'),
    path ('presupuesto-rubro/', views.presupuesto_rubro, name='presupuesto_rubro'),
    path ('consultar-ocupantes/', views.consultar_ocupantes, name='consultar_ocupantes'),
    path ('consultar-visitante/', views.consultar_visitantes, name= 'consultar_visitante'),
    path ('registro-usuarios/', Vista_Registro.as_view(), name='registro_usuarios'),
    path ('modificar-ocupante/<id>/', views.modificar_ocupante, name='modificar_ocupante'),
    path ('eliminar-ocupante/<id>/', views.eliminar_ocupante, name='eliminar_ocupante'),
    path('consultar-presupuesto/', views.consultar_presupuesto, name='consultar_presupuesto'),
    path('modificar-rubro/<id>/', views.modificar_rubro, name='modificar_rubro'),
    path ('eliminar-rubro/<id>/', views.eliminar_rubro, name='eliminar_rubro'),
    path ('500/', views.error, name='500'),
    
    
]