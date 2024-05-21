from django.contrib import admin
from django.urls import path, include
from .views import bienvenido

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path("app1/", include ("app1.urls")),
    
]
