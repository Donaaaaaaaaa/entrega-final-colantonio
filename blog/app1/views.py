from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, "home.html")

def app1_view(request):
    return render(request, "template.html")

def blog1_view(request):
    return render(request, "barcelona.html")

def acercade_view(request):
    return render(request, "acerca_de.html")

def contacto_view(request):
    return render(request, "contacto.html")