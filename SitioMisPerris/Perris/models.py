from django.db import models

# Create your models here.

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40,default='null')
    raza_predominante = models.CharField(max_length=40,default='null')
    descripcion = models.CharField(max_length=50,default='null')
    estado = models.CharField(max_length=15,default='null')
    foto = models.ImageField(default='hola')