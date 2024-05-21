from django.urls import path
from .views import (
    PantalonDelete, PrendaCreacion, PantalonDetalle, CamisaLista, RemeraLista,
    CamperaLista, BusoLista, MediaLista, ZapatillaLista, PantalonLista, 
    CamisaDetalle, RemeraDetalle, CamperaDetalle, BusoDetalle, MediaDetalle, 
    ZapatillaDetalle, PantalonUpdate, CamisaUpdate, RemeraUpdate, CamperaUpdate, 
    BusoUpdate, MediaUpdate, ZapatillaUpdate, CamisaDelete, RemeraDelete, 
    CamperaDelete, BusoDelete, MediaDelete, ZapatillaDelete, login, registro, 
    usuario, CambioPassword, inicio, ComentarioPagina, about
)
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', inicio.as_view(), name='home'),

    path('login/', login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', registro.as_view(), name='registro'),
    path('edicionPerfil/', usuario.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaPantalones/', PantalonLista.as_view(), name='pantalones'),
    path('listaCamisas/', CamisaLista.as_view(), name='camisas'),
    path('listaRemeras/', RemeraLista.as_view(), name='remeras'),
    path('listaCamperas/', CamperaLista.as_view(), name='camperas'),
    path('listaBusos/', BusoLista.as_view(), name='busos'),
    path('listaMedias/', MediaLista.as_view(), name='medias'),
    path('listaZapatillas/', ZapatillaLista.as_view(), name='zapatillas'),

    path('pantalonDetalle/<int:pk>/', PantalonDetalle.as_view(), name='pantalon'),
    path('camisaDetalle/<int:pk>/', CamisaDetalle.as_view(), name='camisa'),
    path('remeraDetalle/<int:pk>/', RemeraDetalle.as_view(), name='remera'),
    path('camperaDetalle/<int:pk>/', CamperaDetalle.as_view(), name='campera'),
    path('busoDetalle/<int:pk>/', BusoDetalle.as_view(), name='buso'),
    path('mediaDetalle/<int:pk>/', MediaDetalle.as_view(), name='media'),
    path('zapatillaDetalle/<int:pk>/', ZapatillaDetalle.as_view(), name='zapatilla'),

    path('pantalonEdicion/<int:pk>/', PantalonUpdate.as_view(), name='pantalon_editar'),
    path('camisaEdicion/<int:pk>/', CamisaUpdate.as_view(), name='camisa_editar'),
    path('remeraEdicion/<int:pk>/', RemeraUpdate.as_view(), name='remera_editar'),
    path('camperaEdicion/<int:pk>/', CamperaUpdate.as_view(), name='campera_editar'),
    path('busoEdicion/<int:pk>/', BusoUpdate.as_view(), name='buso_editar'),
    path('mediaEdicion/<int:pk>/', MediaUpdate.as_view(), name='media_editar'),
    path('zapatillaEdicion/<int:pk>/', ZapatillaUpdate.as_view(), name='zapatilla_editar'),

    path('pantalonBorrado/<int:pk>/', PantalonDelete.as_view(), name='pantalon_eliminar'),
    path('camisaBorrado/<int:pk>/', CamisaDelete.as_view(), name='camisa_eliminar'),
    path('remeraBorrado/<int:pk>/', RemeraDelete.as_view(), name='remera_eliminar'),
    path('camperaBorrado/<int:pk>/', CamperaDelete.as_view(), name='campera_eliminar'),
    path('busoBorrado/<int:pk>/', BusoDelete.as_view(), name='buso_eliminar'),
    path('mediaBorrado/<int:pk>/', MediaDelete.as_view(), name='media_eliminar'),
    path('zapatillaBorrado/<int:pk>/', ZapatillaDelete.as_view(), name='zapatilla_eliminar'),

    path('prendaCreacion/', PrendaCreacion.as_view(), name='nueva_prenda'),

    path('pantalonDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('camisaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('remeraDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('camperaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('busoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('mediaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('zapatillaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
]

# app1/urls.py
from django.urls import path
from .views import PantalonLista

urlpatterns = [
    path('pantalones/', PantalonLista.as_view(), name='pantalon_lista'),
]