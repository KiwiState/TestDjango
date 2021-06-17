from django.db import models
##toma el usuario de este momento
from django.contrib.auth.models import User

class  Usuarios(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='Id',null = True)
    nombre = models.CharField(max_length=128,verbose_name='Nombre',null = True)
    correo = models.EmailField(max_length=200,verbose_name='Email',null = True)
    sexo = models.CharField(max_length=6,verbose_name='Sexo',null = True)
    edad = models.IntegerField(verbose_name='edad',null = True)
    artista = models.BooleanField(verbose_name='artista',null = True)
    def __str__(self):
        return self.nombre

class  Contacto(models.Model):
    email       = models.EmailField(primary_key=True,verbose_name='email',null = True)
    titulo      = models.CharField(max_length=128,verbose_name='titulo',null = True)
    descripcion = models.CharField(max_length=500,verbose_name='descripcion',null = True)       

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True,verbose_name='Id Categoria',null = True)
    nombreCategoria = models.CharField(max_length=60,verbose_name='Concepto',null = True)
    def __str__(self):   
        return self.nombreCategoria

class  Pintura(models.Model):
    id_pintura = models.IntegerField(primary_key=True,verbose_name='Id Pintura',null = True)
    titulo = models.CharField(max_length=200,verbose_name='titulo',null = True)
    id = models.ForeignKey(Usuarios,on_delete=models.CASCADE,verbose_name='Id',null = True)
    descripcion = models.CharField(max_length=500,verbose_name='descripcion',null = True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null = True)
    fecha = models.DateField(verbose_name='fecha',null = True)
    imagen = models.ImageField(null=True,blank=True,verbose_name='imagen')
    def __str__(self):   
        return self.titulo

# Create your models here.
##class Categoria(models.Model):
##    idCategoria=models.IntegerField(primary_key=true,verbose_name='Id Categoria')
##    nombreCategoria = models.CharField(max_lenght=58,verbose_name='Nombre de la Categoria')

##    def __str__(self):
##        return self.nombreCAtegoria
##class Vehiculo(models.model):
##    patente=models.CharField(max_lenght=6,primary_key=true,verbose_name='Patente') 
##    marca=models.CharField(max_lenght=20,verbose_name='Marca del vehiculo')
##    modelo=models.CharField(max_lenght=20,null=true,blank=true,verbose_name='Modelo')   
##    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)

##    def __str__(self):
##        return self.patent e