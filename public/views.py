from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from public.forms import *
from public.models import *

def index(request):
	context = {}
	return render(request, '../templates/index.html', context)

def mainPage(request):
	context = {}
	return render(request, '../templates/mainPage.html', context)
