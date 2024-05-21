from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Prenda, Comentario
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Prenda, Comentario
from .forms import FormularioRegistroUsuario, FormularioEdicion, ActualizacionPrenda, FormularioComentario, FormularioCambioPassword, FormularioNuevoPrenda

class inicio(LoginRequiredMixin, TemplateView):
    template_name = 'inicio.html'

class login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class registro(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(registro, self).get(*args, **kwargs)

class usuario(UpdateView):
    form_class = FormularioEdicion
    template_name = 'usuario.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})

# PANTALONES

class PantalonLista(LoginRequiredMixin, ListView):
    context_object_name = 'pantalones'
    queryset = Prenda.objects.filter(Prenda__startswith='Pantalon')
    template_name = 'listaPantalones.html'
    login_url = '/login/'

class PantalonDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'pantalon'
    template_name = 'pantalonDetalle.html'

class PantalonUpdate(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = ActualizacionPrenda
    success_url = reverse_lazy('pantalones')
    context_object_name = 'pantalon'
    template_name = 'pantalonesEdicion.html'

class PantalonDelete(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('pantalones')
    context_object_name = 'pantalon'
    template_name = 'pantalonBorrado.html'

# CAMISAS

class CamisaLista(LoginRequiredMixin, ListView):
    context_object_name = 'camisas'
    queryset = Prenda.objects.filter(Prenda__startswith='Camisa')
    template_name = 'listaCamisa.html'

class CamisaDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'camisa'
    template_name = 'camisaDetalle.html'

class CamisaUpdate(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = ActualizacionPrenda
    success_url = reverse_lazy('camisas')
    context_object_name = 'camisa'
    template_name = 'camisaEdicion.html'

class CamisaDelete(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('camisas')
    context_object_name = 'camisa'
    template_name = 'camisaBorrado.html'

# REMERAS

class RemeraLista(LoginRequiredMixin, ListView):
    context_object_name = 'remeras'
    queryset = Prenda.objects.filter(Prenda__startswith='Remera')
    template_name = 'listaRemera.html'

class RemeraDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'remera'
    template_name = 'RemeraDetalle.html'

class RemeraUpdate(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = ActualizacionPrenda
    success_url = reverse_lazy('remeras')
    context_object_name = 'remera'
    template_name = 'remeraEdicion.html'

class RemeraDelete(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('remeras')
    context_object_name = 'remera'
    template_name = 'remeraBorrado.html'

# CAMPERAS

class CamperaLista(LoginRequiredMixin, ListView):
    context_object_name = 'camperas'
    queryset = Prenda.objects.filter(Prenda__startswith='Campera')
    template_name = 'listaCampera.html'

class CamperaDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'campera'
    template_name = 'camperaDetalle.html'

class CamperaUpdate(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = ActualizacionPrenda
    success_url = reverse_lazy('campera')
    context_object_name = 'prenda'
    template_name = 'camperaEdicion.html'

class CamperaDelete(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('camperas')
    context_object_name = 'campera'
    template_name = 'camperaBorrado.html'

# BUSOS

class BusoLista(LoginRequiredMixin, ListView):
    context_object_name = 'busos'
    queryset = Prenda.objects.filter(Prenda__startswith='Buso')
    template_name = 'listaBuso.html'

class BusoDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'buso'
    template_name = 'busoDetalle.html'

class BusoUpdate(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = ActualizacionPrenda
    success_url = reverse_lazy('prendas')
    context_object_name = 'buso'
    template_name = 'busoEdicion.html'

class BusoDelete(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('busos')
    context_object_name = 'buso'
    template_name = 'busoBorrado.html'

# MEDIAS

class MediaLista(LoginRequiredMixin, ListView):
    context_object_name = 'medias'
    queryset = Prenda.objects.filter(Prenda__startswith='Media')
    template_name = 'listaMedia.html'

class MediaDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'media'
    template_name = 'mediaDetalle.html'

class MediaUpdate(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = ActualizacionPrenda
    success_url = reverse_lazy('medias')
    context_object_name = 'media'
    template_name = 'mediaEdicion.html'

class MediaDelete(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('medias')
    context_object_name = 'media'
    template_name = 'mediaBorrado.html'

# ZAPATILLAS

class ZapatillaLista(LoginRequiredMixin, ListView):
    context_object_name = 'zapatillas'
    queryset = Prenda.objects.filter(Prenda__startswith='Zapatilla')
    template_name = 'listaZapatilla.html'

class ZapatillaDetalle(LoginRequiredMixin, DetailView):
    model = Prenda
    context_object_name = 'zapatilla'
    template_name = 'zapatillaDetalle.html'

class ZapatillaUpdate(LoginRequiredMixin, UpdateView):
    model = Prenda
    form_class = ActualizacionPrenda
    success_url = reverse_lazy('zapatillas')
    context_object_name = 'zapatilla'
    template_name = 'zapatillaEdicion.html'

class ZapatillaDelete(LoginRequiredMixin, DeleteView):
    model = Prenda
    success_url = reverse_lazy('zapatillas')
    context_object_name = 'zapatilla'
    template_name = 'zapatillaBorrado.html'

# CREACION PRENDA

class PrendaCreacion(LoginRequiredMixin, CreateView):
    model = Prenda
    form_class = FormularioNuevoPrenda
    success_url = reverse_lazy('home')
    template_name = 'prendaCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PrendaCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'acercaDeMi.html', {})

   
