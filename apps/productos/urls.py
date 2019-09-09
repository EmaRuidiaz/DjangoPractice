from django.contrib import admin
from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('listar/', views.ListarProductos, name="listar"),
    path('detalle/<int:codigo>', views.DetalleProducto, name="detalle"),
    path('agregar/', views.AgregarProducto, name="agregar"),
    path('modificar/<int:codigo>', views.ModificarProducto, name="modificar"),
    path('eliminar/<int:codigo>', views.EliminarProducto, name="eliminar")
]