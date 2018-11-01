from django.db import models
from Perris.choices import ESTADO_PERRO

# Create your models here.

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40,default='null')
    raza_predominante = models.CharField(max_length=40,default='null')
    descripcion = models.CharField(max_length=50,default='null')
    estado = models.IntegerField(choices=ESTADO_PERRO, default=1)
    foto = models.ImageField(upload_to='Perris/', blank=True)