
from django.contrib.auth import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Propias

from .views import*
from . import views
from .views import Vista_Ot

urlpatterns = [

    
    path('', views.menu, name='menu'),
    path('ingresar-sistema/', views.ingresar_sistema, name='ingresar_sistema'),
    path('ingresar-elemento/', views.ingresar_elemento, name='ingresar_elemento'),
    path('consultar-elemento/', views.consultar_elemento, name='consultar_elemento'),
    path('eliminar-elemento/<id>', views.eliminar_elemento, name= 'eliminar_elemento'),
    path('modificar-elemento/<id>', views.modificar_elemento, name= 'modificar_elemento'),
    path('ver-elemento/<id>', views.ver_elemento, name= 'ver_elemento'),
    path('preventivo-elemento/', views.preventivo, name='preventivo'),
    path('correctivo-elemento/', views.correctivo, name='correctivo'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ot/crear/',  Vista_Ot.crear_ot, name='crear_ot'),
    path('ot/mostrar/',  Vista_Ot.mostrar_ot, name='mostrar_ot'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)