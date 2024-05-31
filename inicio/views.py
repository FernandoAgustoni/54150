from django.http import HttpResponse
from datetime import datetime

def inicio (request):
    return HttpResponse ("SOY leproso hasta los huevos")

# Create your views here.

def template1 (request,nombre,apellido):
   fecha = datetime.now()
   return HttpResponse(f"Mi template 1 -- Fecha: {fecha} -- Buenas {nombre} {apellido}")