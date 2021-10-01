from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import BLANK_CHOICE_DASH, EmailField
from django.forms import widgets
from django.utils import tree

# Create your models here.

class Edificio_Model (models.Model):
    creado = models.DateField(auto_now=True)
    nombre = models.CharField(max_length= 20)
    ubicacion = models.CharField(max_length=50)
    nit = models.CharField(max_length=15)
    contacto = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) :
        return self.nombre



opciones_estado = [
    [0, 'Disponible'],
    [1, 'Ocupado']

]

opciones_cuenta =[
    [0, 'Propietario'],
    [1, 'Ocupante']

]

class Propietario_Model(models.Model):
    nombre = models.CharField(max_length=30)
    edificio = models.ForeignKey(Edificio_Model, on_delete=models.PROTECT)
    tipo = models.BooleanField(choices=opciones_cuenta)
    apartamento = models.CharField(max_length=5)
    correo = models.EmailField()
    contacto_1 = models.CharField(max_length=14)
    contacto_2 = models.CharField(max_length=14, blank=True)
    estado = models.BooleanField(choices=opciones_estado)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.apartamento



opcion_vehiculo =[

    [0, "Carro"],
    [1, "Moto"]

]


class Visitante_Model(models.Model):
    nombre = models.CharField(max_length=30)
    apartamento = models.ForeignKey(Propietario_Model, on_delete=models.CASCADE)
    vehiculo = models.BooleanField(choices=opcion_vehiculo, blank= True)
    placa = models.CharField(max_length=14, blank=True)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre



class Presupuesto_Cuenta(models.Model):
    nombre = models.CharField(max_length=50)
    creado = models.TimeField(auto_now=True)

    def __str__(self):
        return self.nombre



opciones_frecuencia = [
    [1, 'Mesual'],
    [2, 'Semestral'],
    [3, 'Trimestral'],
    [4, 'Cuatrimestral'],
    [5, 'Semestral'],
    [6, 'Anual']
    
]

opciones_mes = [
    [1, 'Enero'],
    [2, 'Febrero'],
    [3, 'Marzo'],
    [4, 'Abril'],
    [5, 'Mayo'],
    [6, 'Junio'],
    [7, 'Julio'],
    [8, 'Agosto'],
    [9, 'Septiembre'],
    [10, 'Octubre'],
    [11, 'Noviembre'],
    [12, 'Diciembre'],
    
]


class Presupuesto_Rubro(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Presupuesto_Cuenta, on_delete=models.PROTECT)
    frecuencia = models.IntegerField(default=0, choices=opciones_frecuencia)
    mes = models.IntegerField(choices=opciones_mes)
    valor = models.DecimalField(max_digits=14, decimal_places=3)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


    



