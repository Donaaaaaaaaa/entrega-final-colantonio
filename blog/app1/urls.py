
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .views import home_view, app1_view, blog1_view, acercade_view, contacto_view

urlpatterns = [
    path('acerca-de/', acercade_view),
    path('contacto/', contacto_view),
    path('blog/barcelona/', blog1_view),
    path('inicio/', home_view),
    path('seleccion/', app1_view)
]