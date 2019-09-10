from django.shortcuts import render, redirect
from .models import Rubro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ListarRubros(ListView):
	model = Rubro
	template_name = 'Rubro/listarRubros.html'

class DetalleRubro(DetailView):
	model = Rubro
	template_name = 'Rubro/detalle.html'

class AgregarRubro(CreateView): #Vistas basadas en clases
	model = Rubro
	template_name = 'Rubro/agregar.html'
	success_url = reverse_lazy('rubros:listar')
	fields = '__all__'

class ModificarRubro(UpdateView):
	model = Rubro
	template_name = 'Rubro/agregar.html'
	success_url = reverse_lazy('rubros:listar')
	fields = '__all__'

class EliminarRubro(DeleteView):
	model = Rubro
	template_name = 'Rubro/eliminar.html'
	success_url = reverse_lazy('rubros:listar')