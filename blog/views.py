from django.shortcuts import render
from http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('hello')
