from django.shortcuts import render,redirect
from .forms import PinturaForm,UsuariosForm,ContactoForm,Pintura,Usuarios
# Create your views here.
def home(request):
    return render(request,'core/index.html')

def artistas(request):
    usuarios = Usuarios.objects.all()
    datos = {
        'usuarios': usuarios
    }
    return render(request,'core/artistas.html',datos)

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
    return render(request,'core/contacto.html',datos)      

def galeria(request):
    pintura = Pintura.objects.all()
    datos = {
        'pintura': pintura
    }
    return render(request,'core/galeria.html',datos)

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
    
def form_mod_pintura(request, id):
    pintura = Pintura.objects.get(id_pintura=id)
    datos ={ 'form' : PinturaForm(instance=pintura)}
    if request.method == 'POST':
        formulario = PinturaForm(data=request.POST,instance=pintura)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request,'core/modificar_pinturas.html',datos)

def registro(request):

    datos ={'form' :UsuariosForm}
    
    if request.method=='POST':
        
        formulario = UsuariosForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente" 

    return render(request,'core/registro.html',datos)
def subirobra(request):
    
    datos ={'form' :PinturaForm}
    
    if request.method=='POST':
        formulario = PinturaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente" 
    return render(request,'core/subirobra.html',datos)
    
def form_list_mod_pintura(request):   
    pintura = Pintura.objects.all()
    datos = {
        'pintura': pintura
    }
    return render(request,'core/listar_pinturas_modificar.html',datos)

def form_del_pintura(request,id):   
    pintura = Pintura.objects.get(id_pintura=id)
    pintura.delete()
    return redirect(to="form_mod_list_pintura")

def pintura_fill(request, id):
    pintura = Pintura.objects.get(id_pintura=id)
    datos = {
        'pintura': pintura
    }
    return render(request,'core/Pintura_autofill.html',datos)
     
    
          
