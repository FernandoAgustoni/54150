from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Auto
import random
from inicio.forms import CrearAutosFormulario

def inicio (request):
    return render (request,"inicio")

# Create your views here.

def template1 (request,nombre,apellido,edad):
   fecha = datetime.now()
   suma = 4 + edad
   return HttpResponse(f"<h1>Mi template 1</h1> -- Fecha: {fecha} -- Buenas {nombre} {apellido} {edad}")

def template4 (request,nombre,apellido,edad):
   
    
   
    
    fecha = datetime.now()
    
    datos= {
        "fecha": fecha,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad
    }
    
  
    
    
    return render(request,"template4.html", datos)


def probando (request):
    
    lista = list (range(500))
    
    numeros= random.choices (lista, k=50)
    
    return render (request, "probando.html", {"numeros": numeros})

def crear_auto (request, marca, modelo):
    auto = Auto (marca= marca, modelo = modelo)
    auto.save ()
    return render(request,"auto-template/creacion.html", {"auto": auto})

def crear_auto_V2 (request):
    
    print ("valor de la request; ", request)
    print ("valor de GET; ", request.GET)
    print ("valor de POST; ", request.POST)
    
    formulario = CrearAutosFormulario()
    
    if request.method == "POST":
      formulario = CrearAutosFormulario(request.POST)
      if formulario.is_valid ():
       datos = formulario.cleaned_data   
       auto= Auto (marca=datos.get ("marca"), modelo= datos.get ("modelo"))
       auto.save()
       return redirect ("autos")
    
   
    return render (request, "inicio/crear_auto_V2.html",{"formulario": formulario} )

def autos(request):
    
    autos= Auto.objects.all ()
    
    
    return render (request,"inicio/autos.html", {"autos":autos})