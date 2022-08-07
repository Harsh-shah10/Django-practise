from django.urls import path
from .views import *

urlpatterns = [
	path('',index,name='index'),
	path('contactus/',contact,name='contact'),
	path('stock/',stock,name='inventory'),
	path('stockdb/',dbstock,name='db stock'),
	path('home/',home,name='home'),
]