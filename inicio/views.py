from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def inicio (request):
    return HttpResponse ("SOY leproso hasta los huevos")

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
