from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(req):
    return JsonResponse("Hello, World!", safe= False)
