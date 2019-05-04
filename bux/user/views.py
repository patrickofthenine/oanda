from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	user = 'user route res'
	return HttpReponse(user)

def signin(request):
	signin = 'signin route res'
	return HttpResponse(signin)
