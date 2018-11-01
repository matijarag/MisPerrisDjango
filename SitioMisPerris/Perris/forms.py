from .models import Mascota
from django import forms
from Perris.choices import ESTADO_PERRO

class regMascotia (forms.Form):
    nombre = forms.CharField()
    raza_predominante = forms.CharField()
    descripcion = forms.CharField()
    estado = forms.ChoiceField(choices = ESTADO_PERRO, widget=forms.Select())
    foto = forms.ImageField()