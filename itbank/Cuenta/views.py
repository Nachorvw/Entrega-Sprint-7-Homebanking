from django.shortcuts import render

# Create your views here.
def dolar(request):
    return render(request, "Cuenta/dolarsi.html")