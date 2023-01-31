from django.db import models

# Create your models here.

#Modelo para la Categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCatgoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoría')
    def __str__(self):
        return self.nombreCatgoria

#Modelo para el Vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=15, primary_key=True, verbose_name='Nombre')
    marca = models.CharField(max_length=15, verbose_name='Raza')
    modelo = models.CharField(max_length=2, null=True, verbose_name='edad')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    def __str__(self):
        return self.patente
