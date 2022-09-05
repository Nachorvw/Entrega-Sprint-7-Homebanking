from django.contrib import admin
from Cliente.models import *

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Usuarios)
admin.site.register(Prestamo)