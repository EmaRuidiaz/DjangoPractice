from django.db import models
from apps.rubro.models import Rubro

# Create your models here.

class Productos(models.Model):
	nombre = models.CharField(max_length=30)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField()
	imagen = models.ImageField(upload_to = 'productos', null = True)
	rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE, related_name='productosXrubro')

	def __str__(self):
		return self.nombre


