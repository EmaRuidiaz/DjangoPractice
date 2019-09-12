from django.contrib import admin
from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('listar/', views.ListarProductos.as_view(), name="listar"),
    path('detalle/<int:pk>', views.DetalleProducto.as_view(), name="detalle"),
    path('agregar/', views.AgregarProducto.as_view(), name="agregar"),
    path('modificar/<int:pk>', views.ModificarProducto.as_view(), name="modificar"),
    path('eliminar/<int:pk>', views.EliminarProducto.as_view(), name="eliminar"),
    path('productos/<int:rubro>', views.ListarProductosPorRubro, name="porrubro"),
]