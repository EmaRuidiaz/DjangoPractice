from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
	return render(request,'start.html')

def login(request):
	return render(request, 'login.html')