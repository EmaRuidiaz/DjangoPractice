from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from apps.rubro.models import Rubro
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def inicio(request):
	return render(request,'start.html')

def login(request):
	return render(request, 'login.html')

class ListarRubrosHome(LoginRequiredMixin,ListView):
	model = Rubro
	template_name = 'start.html'