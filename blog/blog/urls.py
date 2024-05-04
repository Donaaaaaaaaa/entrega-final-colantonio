"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def mi_func(xx):
    return HttpResponse("<a href='/app1/inicio/' style='color: red; font-size: 150px;'>click aqui para entrar en la app!</a>")

def app1_view(request):
    contexto_dict = {
        'players': [
         
        ]
    }


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mi_func),
    path("app1/", include ("app1.urls")),
    path('list/', app1_view)
]
