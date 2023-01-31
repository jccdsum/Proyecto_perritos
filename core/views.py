from django.shortcuts import render, redirect
from .models import Vehiculo, Categoria
from .forms import VehiculoForm


# Create your views here.
# def home(request):
#     vVehiculos = Vehiculo.objects.all()
#     datos = {'vehiculos':vVehiculos}
#     return render(request, 'home.html', datos)

def form_perrito(request):
    datos ={
        'form':VehiculoForm()
        }
    if request.method=='POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardados correctamente"
    return render(request, 'form_perrito.html',datos)


def crud(request):
    vVehiculos = Vehiculo.objects.all()
    contexto = {'nombre':'Héctor y Jorge', 'vehiculos':vVehiculos}
    return render(request, 'crud.html', contexto)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {
        'form':VehiculoForm(instance=vehiculo)
    }
    if request.method=='POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Registro Actualizado correctamente"
    return render(request,'form_mod_vehiculo.html', datos)

def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="home")

def chloe(request):
    return render(request, 'chloe.html')

def estrella(request):
    return render(request, 'estrella.html')

def gatos(request):
    return render(request, 'gatos.html')

def gusgus(request):
    return render(request, 'Gusgus.html')

def index(request):
    
    return render(request, 'index.html')

def lucas(request):
    return render(request, 'lucas.html')

def pelusa(request):
    return render(request, 'pelusa.html')

def perros(request):
    return render(request, 'perros.html')

def philip(request):
    return render(request, 'philip.html')

def princesa(request):
    return render(request, 'princesa.html')

def samantha(request):
    return render(request, 'samantha.html')

def form_contacto(request):
    return render(request, 'form-contacto.html')
