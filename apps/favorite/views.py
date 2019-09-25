from django.shortcuts import render, redirect
from apps.favorite.models import Favorite
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from apps.productos.models import Productos
# Create your views here.

class AddFavorite(CreateView):
	model = Favorite
	
	success_url = reverse_lazy('productos:porrubro')
	fields = '__all__'

def AddFavorite(request, pk): #Vistas basadas en funciones
	
	producto = Productos.objects.get(pk = pk)

	try:
		check = Favorite.objects.get(producto = producto, user = request.user)
	except:
		check = None
	
	print(check)
	if not check:
		fav = Favorite.objects.create(producto = producto, user = request.user)
		fav.save()
	else:
		fav = Favorite.objects.get(producto = producto, user = request.user).delete()
			
	return redirect('productos:porrubro')

	

