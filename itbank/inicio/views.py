from django.shortcuts import render, HttpResponse, redirect
from inicio.Form import ContactForm
from django.urls import reverse
from inicio.models import Pre
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request, "inicio/navbar.html")


@login_required
def formulario(request):
    Contact_form = ContactForm()
    print("hola")
    if request.method == "POST":
        print("da")

        if Contact_form.is_valid():

            prestamo = request.POST['prestamo']
            clase = request.POST['clase']
            Monto = request.POST['Monto']
            fecha = request.POST['fecha']

        ppp = Pre(tipo=request.POST['prestamo'], monto=request.POST['Monto'],
                  cliente=request.POST['clase'], fecha=request.POST['fecha'])

        ppp.save()
        print(ppp)
        return render(request, "Cuenta/dolarsi.html", {'form': Contact_form})
    return render(request, "inicio/navbar.html", {'form': Contact_form})
