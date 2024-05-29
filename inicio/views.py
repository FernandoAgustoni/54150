from django.http import HttpResponse


def inicio (request):
    return HttpResponse ("SOY leproso hasta los huevos")

# Create your views here.

def template1 (request):
   return HttpResponse ("Mi template 1")