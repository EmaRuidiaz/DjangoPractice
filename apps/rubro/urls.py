from django.contrib import admin
from django.urls import path
from . import views

app_name = "rubros"

urlpatterns = [
    path('listar/', views.ListarRubros.as_view(), name="listar"),
    path('detalle/<int:pk>', views.DetalleRubro.as_view(), name="detalle"),
    path('agregar/', views.AgregarRubro.as_view(), name="agregar"),
    path('modificar/<int:pk>', views.ModificarRubro.as_view(), name="modificar"),
    path('eliminar/<int:pk>', views.EliminarRubro.as_view(), name="eliminar")
]