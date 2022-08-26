from django import forms

class ContactForm(forms.Form):
    tipo=forms.CharField(label="tipo_prestamo")
    monto=forms.CharField(label="Monto")
    cliente=forms.CharField(label="clase")
    fecha=forms.CharField(label="fecha")