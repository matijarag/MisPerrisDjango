from django.db import models
from time import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('Debe ingresar email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email,password, False, False, **extra_fields)
    
    def create_superuser(self,email,password,**extra_fields):
        return self._create_user(email,password,True,True,**extra_fields)
    
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, unique=True)
    fechaNac = models.CharField(max_length=10, blank=True)
    comuna = models.CharField(max_length=10, blank=True)
    tipo_vivienda = models.CharField(max_length=20, blank=True)
    telefono = models.CharField(max_length=20,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','comuna', 'tipo_vivienda','telefono']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')
    
    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        nombre_completo = '%s %s' % (self.nombre, self.apellido)
        return nombre_completo.strip()
    
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
