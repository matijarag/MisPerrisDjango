from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota
from Perris.forms import regMascotia

# Create your views here.

def index(request):
    form_mascota = regMascotia(request.POST or None,request.FILES)
    variable = {
       "form":form_mascota
    }
    if form_mascota.is_valid():
        datos = form_mascota.cleaned_data
        nombre = datos.get("nombre")
        raza_predominante = datos.get("raza_predominante")
        descripcion = datos.get("descripcion")
        estado = datos.get("estado")
        foto = datos.get("foto")
        db_mascota = Mascota(nombre=nombre, raza_predominante=raza_predominante, descripcion=descripcion, estado=estado, foto=foto)
        db_mascota.save()
    return render(request,'index.html',variable)