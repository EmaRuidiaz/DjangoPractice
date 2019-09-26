from django.shortcuts import render, redirect
from .models import Productos, Rubro
from apps.favorite.models import Favorite
from .forms import ProductosForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

'''def ListarProductos(request):
	p  = Productos.objects.all()
	pp = Productos.objects.filter(stock=10)
	ppp = Productos.objects.get(pk = 1)
	context = {}
	context['Productos'] = p
	context['Cantidad'] = p.count()
	return render(request, 'Productos/listarProductos.html',context)'''

class ListarProductos(LoginRequiredMixin,ListView):
	model = Productos
	template_name = 'Productos/listarProductos.html'

'''@login_required
def ListarProductosPorRubro(request, rubro):
	context = {}
	context['object_list'] = Productos.objects.filter(rubro = rubro)
	
	#r = Rubro.objects.get(pk=rubro)
	#context['object_list'] = r.productosXrubro.all()
	#return render(request, 'Productos/listarProductos.html', context)
	
	return render(request, 'Productos/listarProductos.html', context)'''

class ListarProductosPorRubro(LoginRequiredMixin, ListView):

	template_name = 'Productos/listarProductos.html'

	def get_queryset(self):
		onlyDisp = self.request.GET.get('disponibles')
		desde = self.request.GET.get('desde', None)
		hasta = self.request.GET.get('hasta', None)
		rubro = self.request.GET.get('filtro', None)

		if not rubro:
			rubro = "0"
		
		if not desde:
			desde = 0
		if not hasta:
			hasta = 9999999999

		if rubro == "0":
			if onlyDisp == "si":
				x = Productos.objects.filter(stock__gt = 0, precio__gte = desde, precio__lte = hasta)
			else:
				x = Productos.objects.filter(precio__gte = desde, precio__lte = hasta)
		else:
			if onlyDisp == "si":
				x = Productos.objects.filter(rubro = rubro, stock__gt = 0, precio__gte = desde, precio__lte = hasta)
			else:
				x = Productos.objects.filter(rubro = rubro, precio__gte = desde, precio__lte = hasta)	
		return x

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubros'] = Rubro.objects.all()

		favorites = Favorite.objects.filter(user = self.request.user).values('producto')

		fav = []
		for p in context['object_list']:
			for i in favorites:
				if p.pk == i['producto']:
					fav.append(p.pk)

		context['favList'] = fav
		
		rubro = self.request.GET.get('filtro', None)
		if not rubro:
			rubro = "0"
		print("Rubro: ", rubro)
		if rubro == "0":
			context['rubroUnico'] = "Todos"
		else:
			context['rubroUnico'] = Rubro.objects.get(id = rubro).nombre
		return context


'''def DetalleProducto(request,codigo):
	context = {}
	context['Productos'] = Productos.objects.get(pk = codigo)
	return render(request, 'Productos/detalle.html',context)'''

class DetalleProducto(LoginRequiredMixin,DetailView):
	model = Productos
	template_name = 'Productos/detalle.html'

'''def AgregarProducto(request): #Vistas basadas en funciones
	form = ProductosForm(request.POST or None, request.FILES)

	if form.is_valid():
		form.save()
		return redirect('productos:listar')

	return render(request, 'Productos/agregar.html', {'form': form})'''

class AgregarProducto(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Productos
	template_name = 'Productos/agregar.html'
	success_url = reverse_lazy('productos:porrubro')
	fields = '__all__'

'''def ModificarProducto(request, codigo):
	producto = Productos.objects.get(id=codigo)
	form = ProductosForm(request.POST or None, request.FILES or None, instance=producto)

	if form.is_valid():
		form.save()
		return redirect('productos:listar')'''

class ModificarProducto(LoginRequiredMixin,UpdateView):
	model = Productos
	template_name = 'Productos/agregar.html'
	success_url = reverse_lazy('productos:porrubro')
	fields = '__all__'

'''def EliminarProducto(request, codigo):
	producto = Productos.objects.get(id=codigo)

	if request.method == 'POST':
		producto.delete()
		return redirect('productos:listar')

	return render(request, 'Productos/eliminar.html', {'Productos':producto})'''

class EliminarProducto(LoginRequiredMixin,DeleteView):
	model = Productos
	template_name = 'Productos/eliminar.html'
	success_url = reverse_lazy('productos:porrubro')