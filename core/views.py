from django.shortcuts import render
from .forms import PinturaForm,UsuariosForm,ContactoForm
# Create your views here.
def home(request):
    return render(request,'core/index.html')

def artistas(request):
    return render(request,'core/artistas.html')

def bs(request):
    return render(request,'core/bs.html')

def concepto(request):
    return render(request,'core/concepto.html')

def contacto(request):
    datos ={'form' :ContactoForm}
    
    if request.method=='POST':
        
        formulario = ContactoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente" 
    return render(request,'core/contacto.html')      

def galeria(request):
    return render(request,'core/galeria.html')

def login(request):
    return render(request,'core/login.html')


def pint1(request):
    return render(request,'core/Pint_1.html')
def pint2(request):
    return render(request,'core/Pint_2.html')
def pint3(request):
    return render(request,'core/Pint_3.html')
def pint4(request):
    return render(request,'core/Pint_4.html')

def registro(request):
    datos ={'form' :UsuariosForm}
    
    if request.method=='POST':
        
        formulario = UsuariosForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente" 

    return render(request,'core/registro.html')
def subirobra(request):
    
    datos ={'form' :PinturaForm}
    
    if request.method=='POST':
        
        formulario = PinturaForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente" 

    return render(request,'core/subirobra.html',datos)
    

          
