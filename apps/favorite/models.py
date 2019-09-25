from django.db import models
from apps.productos.models import Productos
from django.conf import settings

# Create your models here.
class Favorite(models.Model):
	producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='prodfav')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.producto