from django.db import models

class Rubro(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre
# Create your models here.
