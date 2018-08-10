from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("E-lo web, with Django, Gunicorn, Nginx on Digital Ocean. Django Admin testit.tech/admin")

