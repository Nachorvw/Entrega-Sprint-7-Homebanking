from http import client
from multiprocessing.managers import BaseManager
from django.shortcuts import render, HttpResponse, redirect
from inicio.Form import ContactForm
from django.urls import reverse
from Cliente.models import Cuenta, Usuarios
from Cliente.models import Prestamo
from Cliente.models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request, "inicio/navbar.html")

def volver(request):
    return render(request, "Cuenta/dolarsi.html")

@login_required
def formulario(request):
    Contact_form = ContactForm()
    

    if request.method == "POST":
        print(request.user.id)
        print(request.user.id)
        id=request.user.id
        usuario = Usuarios.objects.filter(id = id)
        print(usuario)
        print(usuario[0])
        print(usuario[0].tipo)
        print(usuario[0].Cliente_id)
        balance= Cuenta.objects.filter(customer_id=usuario[0].Cliente_id)
        print(balance)
        print(balance[0].balance)
        if Contact_form.is_valid():

            prestamo = request.POST['prestamo']
            clase = request.POST['clase']
            Monto = request.POST['Monto']
            fecha = request.POST['fecha']

        ppp = Prestamo(loan_type=request.POST['prestamo'], loan_total=request.POST['Monto'],
                  customer_id=usuario[0].id, loan_date=request.POST['fecha'])

        cuenta= Cuenta(account_id=usuario[0].Cuenta_id,customer_id=balance[0].customer_id,balance= int(balance[0].balance) + int(request.POST['Monto']),iban=balance[0].iban)
        print(ppp.customer_id)

        if usuario[0].tipo == "CLASSIC" :
            if int(ppp.loan_total) <= 100000 :
                print("prestamo aprovado")
                ppp.save()
                cuenta.save()
                return redirect(reverse('formulario')+"?ok")
            return redirect(reverse('formulario')+"?no")

        if usuario[0].tipo == "GOLD" :
            if int(ppp.loan_total) <= 300000 :
                print("prestamo aprovado")
                ppp.save()
                cuenta.save()
                return redirect(reverse('formulario')+"?ok")
            return redirect(reverse('formulario')+"?no")

        if usuario[0].tipo == "BLACK" :
            if int(ppp.loan_total) <= 500000 :
                print("prestamo aprovado")
                ppp.save()
                cuenta.save()
                return redirect(reverse('formulario')+"?ok")
            return redirect(reverse('formulario')+"?no")

    return render(request, "inicio/navbar.html", {'form': Contact_form})




