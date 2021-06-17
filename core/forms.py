from django import forms
from django.forms import ModelForm
from .models import Pintura,Contacto,Usuarios

class PinturaForm(ModelForm):
    class Meta:
        model = Pintura
        fields = ['titulo','descripcion','categoria','imagen','id_pintura','id']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['email','titulo','descripcion']

class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','correo','sexo','edad','artista','id']        

     
