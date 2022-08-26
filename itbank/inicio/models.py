from django.db import models

# Create your models here.

class Pre (models.Model):
    tipo=models.CharField(max_length=200)
    monto=models.CharField(max_length=200)
    cliente=models.CharField(max_length=200)
    fecha=models.CharField(max_length=200)

   