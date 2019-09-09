from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
# Create your views here.

def ListarProductos(request):
	p  = Productos.objects.all()
	pp = Productos.objects.filter(stock=10)
	ppp = Productos.objects.get(pk = 1)
	context = {}
	context['Productos'] = p
	context['Cantidad'] = p.count()
	return render(request, 'Productos/listarProductos.html',context)

def DetalleProducto(request,codigo):
	context = {}
	context['Productos'] = Productos.objects.get(pk = codigo)
	return render(request, 'Productos/detalle.html',context)

def AgregarProducto(request):
	form = ProductosForm(request.POST or None, request.FILES)

	if form.is_valid():
		form.save()
		return redirect('productos:listar')

	return render(request, 'Productos/agregar.html', {'form': form})

def ModificarProducto(request, codigo):
	producto = Productos.objects.get(id=codigo)
	form = ProductosForm(request.POST or None, request.FILES or None, instance=producto)

	if form.is_valid():
		form.save()
		return redirect('productos:listar')

	return render(request, 'Productos/agregar.html', {'form': form, 'Productos':producto})

def EliminarProducto(request, codigo):
	producto = Productos.objects.get(id=codigo)

	if request.method == 'POST':
		producto.delete()
		return redirect('productos:listar')

	return render(request, 'Productos/eliminar.html', {'Productos':producto})