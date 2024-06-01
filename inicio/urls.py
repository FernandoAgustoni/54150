from django.urls import path
from inicio import views

urlpatterns = [
    path("",views.inicio),
    path("template1/<str:nombre>/<str:apellido>/<int:edad>",views.template1),
    path("template4/<str:nombre>/<str:apellido>/<int:edad>",views.template4),
    path("probando/",views.probando),
    
]
