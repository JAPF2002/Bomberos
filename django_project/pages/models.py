# En el archivo models.py de la aplicación de inventario
from django.db import models

class Producto(models.Model):
    codigo = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    fecha_de_ingreso = models.DateField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
