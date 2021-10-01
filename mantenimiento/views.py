
import edificios
from edificios.models import Edificio_Model
from os import name
from django.core import paginator
from django.core.checks import messages
from django.db.models.aggregates import Count, Sum
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models.functions import Coalesce
from django.db import models
import pickle

# Create your views here.
from .forms import *
from .models import *


def menu(request):
    edificio = Edificio_Model.objects.all()
    context = {
        'form': edificio
    }
    return render(request, 'mantenimiento/menu.html', context)


def index(request):
   
    return render(request, 'mantenimiento/index.html')


def dashboard(request):
    try:
        data=[]
        data2=[]
        data3=[]
        total_elementos = ElementoModel.objects.count()
        data2.append(int(total_elementos))
        for m in range(0, 8):
            filtro_elementos = ElementoModel.objects.filter(ubicacion=m).count()
            data.append(int(filtro_elementos))
        for m in range(1,len(SistemaModel)):
            filtro_sistema = ElementoModel.objects.filter(id_sistema=m).count()
            data3.append(int(filtro_sistema))
        
    except:
        pass
    context = {
        'data':data,
        'total_elementos': data2,
        'total_sistema' : data3
    }
    return render(request, 'mantenimiento/dashboard.html', context)


def ingresar_sistema(request):

    formulario = SistemaForms
    context ={
        'form':formulario
    }
    if request.method == 'POST':
        formulario = SistemaForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se creo el sistema')
            return redirect('ingresar_sistema')
        else:
            context['form'] = formulario

    return render(request, 'mantenimiento/ingresar-sistema.html', context)


def ingresar_elemento(request):

    formulario = ElementosForms
    
    context ={
        'form':formulario
    }
    if request.method == 'POST':
        formulario = ElementosForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se creo el elemento')
            return redirect('ingresar_elemento')
        else:
            context['form'] = formulario

    return render(request, 'mantenimiento/ingresar-elemento.html', context)


def consultar_elemento(request):
    elementos = ElementoModel.objects.all()
    pagina = request.GET.get('page', 1)
    try:
        paginator = Paginator(elementos, 7)
        elementos = paginator.page(pagina)
    except:
        raise Http404
    context ={
        'entity': elementos,
        'paginator': paginator
    }    
    return render(request, 'mantenimiento/consultar-elemento.html', context)


def eliminar_elemento(request, id):
    elemento = get_object_or_404(ElementoModel, id=id)
    elemento.delete()
    messages.success(request, 'Elemento eliminado con exito')
    return redirect('consultar_elemento')


@permission_required('mantenimiento.elemento_model.delete_elemento_model')
def modificar_elemento(request, id):
    elemento = get_object_or_404(ElementoModel, id=id)
    context ={
        'form': ElementosForms(instance=elemento)
    }
    if request.method == 'POST':
        info_elemento = ElementosForms(data=request.POST, instance=elemento, files=request.FILES)
        if info_elemento.is_valid():
            info_elemento.save()
            messages.success(request, 'Información modificada')
            return redirect('consultar_elemento')
        else:
            messages.Warning(request, 'Los datos no fueron cargados')
    return render(request, 'mantenimiento/modificar-elemento.html', context)


def ver_elemento(request, id):
    pagina = request.GET.get('page', 1)
    elemento = ElementoModel.objects.get(id=id)
    data = PreventivoModel.objects.filter(elemento_id=id)
    try:
        paginator = Paginator(data, 7)
        elementos = paginator.page(pagina)
    except:
        raise Http404
    context ={
        'form': elemento,
        'data': data
    }
    return render(request, 'mantenimiento/ver-elemento.html', context)


def preventivo(request):
    formulario = PreventivoForms()
    context = {
        'form': formulario
    }
    if request.method == 'POST':
        formulario = PreventivoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('preventivo')
        else:
            context['form'] = formulario
    return render(request, 'mantenimiento/preventivo-elemento.html', context)


def correctivo(request):
    formulario = CorrectivoForms()
    context = {
        'form': formulario
    }
    if request.method == 'POST':
        formulario = CorrectivoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('correctivo')
        else:
            context['form'] = formulario
    return render(request, 'mantenimiento/correctivo-elemento.html', context)


