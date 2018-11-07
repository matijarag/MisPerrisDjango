from django.db import models
from RegistroUsu.choices import TIPO_VIVIENDA,COMUNA
# Create your models here.
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12,default='null', unique=True)
    nombre = models.CharField(max_length=40,default='null')
    apellido = models.CharField(max_length=40,default='null')
    fecha_nac = models.DateField(auto_now=True)
    telefono = models.IntegerField(default=1)
    correo = models.EmailField(max_length=100,default='hola@hola.com')
    tipo_vivienda = models.IntegerField(choices=TIPO_VIVIENDA, default=1)
    comuna = models.IntegerField(choices=COMUNA, default=1)
    password = models.CharField(max_length=40, default='pass')