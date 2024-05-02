
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def mi_vista(xx):
    return HttpResponse("<h1 style='color: red; font-size: 150px;'>Bienvenido a app1!</h1>")

urlpatterns = [
    
    path('', mi_vista)
]