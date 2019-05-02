from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import os
# Create your views here.

def index(request):
	print('here', os.getcwd())
	resp = render(request, "price.html")
	return resp