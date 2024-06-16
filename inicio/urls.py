from django.urls import path
from inicio import views

urlpatterns = [   
    path('', views.inicio, name="inicio"),
    path("template1/<str:nombre>/<str:apellido>/<int:edad>",views.template1),
    path("template4/<str:nombre>/<str:apellido>/<int:edad>",views.template4),
    path("prueba/",views.probando, name= "probando"),
    path("autos/crear/<str:marca>/<str:modelo>/",views.crear_auto),
    path("autos/",views.autos, name="autos"),
    path("autos/crear/",views.crear_auto_V2, name="crear_auto_V2"),
    
]  
  
   

