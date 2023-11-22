# En el archivo forms.py de la aplicación de inventario
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'categoria', 'cantidad', 'fecha_de_ingreso', 'imagen']
