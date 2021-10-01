from django.contrib.auth import views
from django.core.exceptions import ImproperlyConfigured
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate



# self 
from .models import*
from .forms import*

# Create your views here.

class Vista_Registro(View):

    def get(seft, request):
        form = UserCreationForm()
        context ={
            'form': form
        }

        return render(request, 'edificios/registro-usuarios.html', context)

    def post(self, request):
        form =UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            messages.success(request, 'Registro exitoso')
            login(request, usuario)

            return redirect('index')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    
        return redirect('500')




def error(request):

    return render(request, 'edificios/500.html')




def index (request):

    return render(request, 'edificios/index.html')




def registro_edificios (request):
    
    context = {

        'form' : EdificioForms
    }

    if request.method == 'POST':
        formulario = EdificioForms(data=request.POST)

        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Registro exitoso')
            return HttpResponseRedirect('/registro-edificios/')

        else:

            context['form'] = formulario


    return render(request, 'edificios/registro-edificios.html', context)




def registro_personas (request):
    
    context = {

        'form' : PropietarioForms
    }

    if request.method == 'POST':

        formulario = PropietarioForms(data=request.POST)

        if formulario.is_valid:
            
            formulario.save()

            return HttpResponseRedirect('/registro-personas/')

        else:

            context['form'] = formulario

    return render(request, 'edificios/registro-personas.html', context)





def registro_visitantes (request):
    
    context = {
        'form' : VisitanteForms
    }

    if request.method == 'POST':
        formulario = VisitanteForms(data=request.POST)

        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/registro-visitantes/')

        else:
            context['form'] = formulario

    return render(request, 'edificios/registro-visitantes.html', context)





def presupuesto_cuenta(request):

    context = {
        'form' : PresupuestoCuentaForms
    }

    if request.method == 'POST':
        formulario = PresupuestoCuentaForms(data=request.POST)

        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/presupuesto-cuenta/')

        else:
            context['form'] = formulario
            
    return render(request, 'edificios/presupuesto-cuenta.html', context)





def presupuesto_rubro(request):


    context = {
        'form' : PresupuestoRubroForms
    }

    if request.method == 'POST':
        formulario = PresupuestoRubroForms(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/presupuesto-rubro/')

        else:
            context['form'] = formulario

    return render(request, 'edificios/presupuesto-rubro.html', context)




def consultar_ocupantes(request):

    formulario = Propietario_Model.objects.all()

    context = {
        'forms': formulario
    }
     
    return render(request, 'edificios/consultar-ocupante.html', context)



def consultar_visitantes(request):

    formulario = Visitante_Model.objects.all()

    context = {
        'forms': formulario
    }

    return render(request, 'edificios/consultar-visitante.html', context)



def consultar_presupuesto(request):
    formulario = Presupuesto_Rubro.objects.all()

    context ={
        'forms': formulario
    }

    return render(request, 'edificios/consultar-presupuesto.html', context)



def ingresar(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasena_usuario = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasena_usuario)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F'Bienvenido {nombre_usuario}')
                return redirect('menu')
            else:
                messages.error(request, 'Información incorrecta')
        else:
            messages.error(request, 'Información incorrecta') 
    
    form = AuthenticationForm()
    context ={
        'form': form

    }

    return render(request, 'edificios/login.html', context)


    
def salir(request):
    
    logout(request)
    messages.success(request, 'Hasta pronto')
    return redirect('login')



def eliminar_ocupante(request, id):
    ocupante = get_object_or_404(Propietario_Model, id=id)
    ocupante.delete()
    return redirect('consultar_ocupantes')




def modificar_ocupante(request, id):

    ocupante =get_object_or_404(Propietario_Model, id=id)

    context ={

        'form': PropietarioForms(instance=ocupante)
    }

    if request.method == 'POST':
        formulario = PropietarioForms(data=request.POST, instance=ocupante)
        if formulario.is_valid():
            formulario.save()
            return redirect('consultar_ocupantes')
        

    return render(request, 'edificios/modificar-ocupante.html', context)




def modificar_rubro(request, id):

    rubro = get_object_or_404(Presupuesto_Rubro, id=id)

    context ={

        'form': PresupuestoRubroForms(instance=rubro)
    }

    if request.method == 'POST':
        formulario = PresupuestoRubroForms(data=request.POST, instance=rubro)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cambio Exitoso')
            return redirect('consultar_presupuesto')
        
    return render(request, 'edificios/modificar-rubro.html', context)

    
def eliminar_rubro(request, id):
    rubro = get_object_or_404(Presupuesto_Rubro, id=id)
    rubro.delete()
    messages.success(request, 'Cambio Exito')
    return redirect('consultar_presupuesto')