from django import forms
from django.forms import ModelForm
from .models import Pintura,Contacto

class PinturaForm(ModelForm):
    class Meta:
        model = Pintura
        fields = ['titulo','descripcion','categoria','imagen','id_pintura','id']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['Email','Titulo','descripción']