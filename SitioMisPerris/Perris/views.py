from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota

# Create your views here.

def index(request):
    Mascotas = Mascota.objects.order_by('-nombre')
    context = {'Mascotas':Mascotas}
    return render(request,'index.html',context)
