from django.db import models

# Create your models here.

class Productos(models.Model):
	nombre = models.CharField(max_length=30)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField()
	imagen = models.ImageField(upload_to = 'productos', null = True)

	def __str__(self):
		return self.nombre


