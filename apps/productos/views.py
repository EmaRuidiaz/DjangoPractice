from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

'''def ListarProductos(request):
	p  = Productos.objects.all()
	pp = Productos.objects.filter(stock=10)
	ppp = Productos.objects.get(pk = 1)
	context = {}
	context['Productos'] = p
	context['Cantidad'] = p.count()
	return render(request, 'Productos/listarProductos.html',context)'''

class ListarProductos(ListView):
	model = Productos
	template_name = 'Productos/listarProductos.html'


'''def DetalleProducto(request,codigo):
	context = {}
	context['Productos'] = Productos.objects.get(pk = codigo)
	return render(request, 'Productos/detalle.html',context)'''

class DetalleProducto(DetailView):
	model = Productos
	template_name = 'Productos/detalle.html'

'''def AgregarProducto(request): #Vistas basadas en funciones
	form = ProductosForm(request.POST or None, request.FILES)

	if form.is_valid():
		form.save()
		return redirect('productos:listar')

	return render(request, 'Productos/agregar.html', {'form': form})'''

class AgregarProducto(CreateView): #Vistas basadas en clases
	model = Productos
	template_name = 'Productos/agregar.html'
	success_url = reverse_lazy('productos:listar')
	fields = '__all__'

'''def ModificarProducto(request, codigo):
	producto = Productos.objects.get(id=codigo)
	form = ProductosForm(request.POST or None, request.FILES or None, instance=producto)

	if form.is_valid():
		form.save()
		return redirect('productos:listar')'''

class ModificarProducto(UpdateView):
	model = Productos
	template_name = 'Productos/agregar.html'
	success_url = reverse_lazy('productos:listar')
	fields = '__all__'

'''def EliminarProducto(request, codigo):
	producto = Productos.objects.get(id=codigo)

	if request.method == 'POST':
		producto.delete()
		return redirect('productos:listar')

	return render(request, 'Productos/eliminar.html', {'Productos':producto})'''

class EliminarProducto(DeleteView):
	model = Productos
	template_name = 'Productos/eliminar.html'
	success_url = reverse_lazy('productos:listar')