from django.shortcuts import render

from django.http import HttpResponse


from .models import *
# Create your views here.

def home(request):
	return HttpResponse('Hey this is homepage')

def index(request):
	return HttpResponse('This is an index')

def contact(request):
	return render(request, 'home.html')

def stock(request):
	fruits = ['Apple', 'Watermelon', 'Orange', 'Pear', 'Cherry', 'Strawberry', 'Nectarine', 'Grape', 'Mango', 'Blueberry', 'Pomegranate', 'Plum', 'Banana', 'Raspberry', 'Mandarin', 'Jackfruit', 'Papaya', 'Kiwi', 'Pineapple', 'Lime', 'Lemon', 'Apricot', 'Grapefruit', 'Melon', 'Coconut', 'Avocado', 'Peach']
	context = {'fruitskey':fruits}
	return render(request,'stock.html',context)	

def dbstock(request):
	context = {'fruitskey':Fruits.objects.all()}
	return render(request,'dbstock.html',context)	
