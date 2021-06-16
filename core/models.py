from django.db import models

class  Usuarios(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='Id',default ='')
    nombre = models.CharField(max_length=128,verbose_name='Nombre',default ='')
    correo = models.EmailField(max_length=200,verbose_name='Email',default ='')
    sexo = models.CharField(max_length=6,verbose_name='Sexo',default ='')
    edad = models.IntegerField(verbose_name='edad',default = 0)
    artista = models.BooleanField(verbose_name='artista',default = 0)
    def __str__(self):
        return self.nombre

##class Categoria(models.Model):
##    idCategoria=models.IntegerField(primary_key=true,verbose_name='Id Categoria')
##    nombreCategoria = models.CharField(max_lenght=58,verbose_name='Concepto')
##    nombreCategoria = models.ForeignKey
##class  Pintura(models.Model):
##    id_pintura = models.IntegerField(primary_key=True,verbose_name='Id',default ='')
##    titulo = models.CharField(max_length=128,verbose_name='Nombre',default ='')
##    id = models.EmailField(max_length=200,verbose_name='Email',default ='')
##    descripcion = models.CharField(max_length=6,verbose_name='Sexo',default ='')
##    categoria = models.IntegerField(verbose_name='edad',default = 0)
##    fecha = models.BooleanField(verbose_name='artista',default = 0)
##    def __str__(self):      
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
##        return self.patente