from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/index.html')    
def galeria(request):
    return render(request,'core/galeria.html')       
def pint1(request):
    return render(request,'core/Pint_1.html')         
