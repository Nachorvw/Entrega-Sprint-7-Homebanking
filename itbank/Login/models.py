from django.db import models

# Create your models here.
class nuevoUsuario(models.Model):
    nombreUsuario=models.CharField(max_length=10)
    contraseña=models.CharField(max_length=10)
    