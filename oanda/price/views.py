from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
# Create your views here.

def index(request):
	resp = render(request, 'price.html')
	print(price_view)
	return resp