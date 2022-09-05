from contextvars import Context
from hashlib import blake2b
from re import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Cliente.models import Cuenta, Usuarios

# Create your views here.


@login_required
def dolar(request):
    #balance= Cuenta.objects.all()
    #print(balance[0].balance)
    id=request.user.id
    usuario = Usuarios.objects.filter(id = id)
    balance= Cuenta.objects.filter(customer_id=usuario[0].Cliente_id)
    print(usuario[0].Cliente_id)
    print(balance)
    print(balance[0].balance)
    monto=balance[0].balance 
    contexto={"cuenta":monto}
    
   

    return render(request, "Cuenta/dolarsi.html",contexto)
