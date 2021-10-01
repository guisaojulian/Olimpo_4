from django import forms
from django.db.models import fields
from django.forms.forms import Form

#self

from .models import *

class PropietarioForms(forms.ModelForm):

    class Meta:
        model = Propietario_Model
        fields = '__all__'


class VisitanteForms(forms.ModelForm):

    class Meta:
        model = Visitante_Model
        fields = '__all__'

class EdificioForms(forms.ModelForm):

    class Meta:
        model = Edificio_Model
        fields = '__all__'


class PresupuestoCuentaForms(forms.ModelForm):

    class Meta:
        model = Presupuesto_Cuenta
        fields = '__all__'


class PresupuestoRubroForms(forms.ModelForm):

    class Meta:
        model = Presupuesto_Rubro
        fields = '__all__'
        