from django import forms
from django.db.models import fields


from .models import *

class SistemaForms(forms.ModelForm):
    class Meta:
        model = SistemaModel
        fields = '__all__'

class ElementosForms(forms.ModelForm):
    class Meta:
        model = ElementoModel
        fields = '__all__'

class PreventivoForms(forms.ModelForm):
    class Meta:
        model = PreventivoModel
        fields = '__all__'

class CorrectivoForms(forms.ModelForm):
    class Meta:
        model = CorrectivoModel
        fields = '__all__'