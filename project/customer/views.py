from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

# Create your views here.
def sign(request):
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def product(request):
    return render(request, 'product.html')

def about(request):
    return render(request, 'about.html')