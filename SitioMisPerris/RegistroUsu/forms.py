from .models import Persona
from django import forms
from RegistroUsu.choices import TIPO_VIVIENDA,COMUNA

class regUsuario(forms.Form):
    rut = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nac = forms.DateField()
    telefono = forms.IntegerField()
    correo = forms.EmailField()
    tipo_vivienda = forms.ChoiceField(choices = TIPO_VIVIENDA, widget=forms.Select())
    comuna = forms.ChoiceField(choices = COMUNA, widget=forms.Select())
    password = forms.CharField(widget=forms.PasswordInput)