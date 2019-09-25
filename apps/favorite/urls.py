from django.contrib import admin
from django.urls import path
from . import views

app_name = "favorite"

urlpatterns = [

    path('agregar/<int:pk>', views.AddFavorite, name="agregar"),
    
]