from django.urls import path
from . import views

urlpatterns = [
	path('user/', 	views.index,  name='index'),
	path('signin/', views.signin, name='signin'),
]