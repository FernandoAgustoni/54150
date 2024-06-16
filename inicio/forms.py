from django import forms

class CrearAutosFormulario (forms.Form):    
    marca = forms.CharField (max_length=20)
    modelo = forms.CharField (max_length=20)
