from django.shortcuts import render, redirect
from .models import Rubro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class ListarRubros(LoginRequiredMixin,ListView):
	model = Rubro
	template_name = 'Rubro/listarRubros.html'

class DetalleRubro(LoginRequiredMixin,DetailView):
	model = Rubro
	template_name = 'Rubro/detalle.html'

class AgregarRubro(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Rubro
	template_name = 'Rubro/agregar.html'
	success_url = reverse_lazy('rubros:listar')
	fields = '__all__'

class ModificarRubro(LoginRequiredMixin,UpdateView):
	model = Rubro
	template_name = 'Rubro/agregar.html'
	success_url = reverse_lazy('rubros:listar')
	fields = '__all__'

class EliminarRubro(LoginRequiredMixin,DeleteView):
	model = Rubro
	template_name = 'Rubro/eliminar.html'
	success_url = reverse_lazy('rubros:listar')