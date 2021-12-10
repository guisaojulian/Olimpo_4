from django.forms import *

class ReporteForms(forms):
    rango_fecha = CharField(widget=TextInput(attrs={
        'class':'form-control',
        'autocomplete':'off'
    }))