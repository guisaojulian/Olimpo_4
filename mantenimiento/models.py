
from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import IntegerField
from django.db.models.fields.files import ImageField

from edificios.models import Edificio_Model

# Create your models here.

class SistemaModel(models.Model):
    creado = models.DateField(auto_now=True)
    sistema = models.CharField(max_length=20)

    def __str__(self):
        return self.sistema

opciones_estado=[
    {0, 'Fuera de servicio'},
    {1, 'En servicio'}
]

opciones_ubicacion= [
    (0, 'Zona común'),
    (1, 'Torre 1'),
    (2, 'Torre 2'),
    (3, 'Torre 3'),
    (4, 'Torre 4'),
    (5, 'Torre 5'),
    (6, 'Torre 6'),
    (7, 'Torre 7')

]
    

class ElementoModel(models.Model):
    creado = models.DateField(auto_now=True)
    edificio = models.ForeignKey(Edificio_Model, on_delete=models.CASCADE)
    ubicacion = models.IntegerField(choices=opciones_ubicacion)
    sistema = models.ForeignKey(SistemaModel, on_delete=models.CASCADE)
    elemento = models.CharField(max_length=50)
    marca = models.CharField(max_length=20)
    referencia = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    estado = models.BigIntegerField(choices=opciones_estado)
    imagen = models.ImageField(upload_to='elementos', null=True, blank = True)

    def __str__(self):
        return self.elemento

opciones_tipo = [ 
        {0, 'Preventivo'},
        {1, 'Correctivo'}
    ]

class PreventivoModel(models.Model):
    creado = models.DateField(auto_now=True, null=True)
    elemento = models.ForeignKey(ElementoModel, on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=opciones_tipo)
    descripcion = models.CharField(max_length=200)
    observacion = models.CharField(max_length=200)
    image = models.ImageField(upload_to='preventivo', null=True, blank=True)

    def __str__(self):
        return self.elemento

class CorrectivoModel(models.Model):
    creado = models.DateField(auto_now=True, null=True)
    elemento = models.ForeignKey(ElementoModel, on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=opciones_tipo)
    descripcion = models.CharField(max_length=200)
    observacion = models.CharField(max_length=200)
    image = models.ImageField(upload_to='correctivo', blank=True)

    def __str__(self):
        return self.elemento



opciones_prioridad =[
    {0, 'Preventivo'},
    {1, 'Correctivo'}
]


class OtModel(models.Model):
    creado = models.DateField(auto_now=True)
    elemento = models.ForeignKey(ElementoModel, on_delete=models.CASCADE)
    tipo = models.BigIntegerField(choices=opciones_prioridad)
    requerido = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(blank=True)
    fecha_fin = models.DateField(blank=True)
    observaciones = models.CharField(max_length=200)

    def __str__(self):
        return self.elemento
