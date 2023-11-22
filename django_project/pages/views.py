from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

class InicioPageView(TemplateView):
    template_name = "inicio.html"

class QuienesPageView(TemplateView):
    template_name = "Quienes.html"

class FormsPageView(TemplateView):
    template_name = "forms.html"

class RegistroPageView(TemplateView):
    template_name = "registro.html"

class Inicio2PageView(TemplateView):
    template_name = "inicio2.html"
class InventarioPageView(TemplateView):
    template_name = "inventario.html"

class Inventario2PageView(TemplateView):
    template_name = "inventario2.html"

