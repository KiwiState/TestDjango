from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=true,verbose_name='Id Categoria')
    nombreCategoria = models.CharField(max_lenght=58,verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCAtegoria
class Vehiculo(models.model):
    patente=models.CharField(max_lenght=6,primary_key=true,verbose_name='Patente') 
    marca=models.CharField(max_lenght=20,verbose_name='Marca del vehiculo')
    modelo=models.CharField(max_lenght=20,null=true,blank=true,verbose_name='Modelo')   
    categoria=models.ForeignKey(categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.patente