from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from RegistroUsu.forms import regUsuario

# Create your views here.
def formulario(request):
    form_usuario = regUsuario(request.POST or None)
    variable = {    
        "formu":form_usuario
    }
    if form_usuario.is_valid():
        data = form_usuario.cleaned_data
        rut = data.get("rut")
        nombre = data.get("nombre")
        apellido = data.get("apellido")
        fecha_nac = data.get("fecha_nac")
        telefono = data.get("telefono")
        correo = data.get("correo")
        tipo_vivienda = data.get("tipo_vivienda")
        comuna = data.get("comuna")
        password = data.get("password")
        db_usuario = Persona(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, telefono=telefono, correo=correo, tipo_vivienda=tipo_vivienda, comuna=comuna, password=password)
        db_usuario.save()
    return render(request,'usuario.html',variable)