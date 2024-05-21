from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import models
from django.contrib.auth.models import User

    
class Prenda(models.Model):
    prendaSeleccion = (
        ('camisa', 'Camisa'),
        ('pantalon', 'Pantalón'),
        ('zapato', 'Zapato'),
        ('chaqueta', 'Chaqueta'),
        ('otro', 'Otro'),
    )
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    imagenPrenda = models.ImageField(upload_to='imagenes/')
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    emailContacto = models.EmailField()
    telefonoContacto = models.CharField(max_length=15)
    year = models.PositiveIntegerField()

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    prenda = models.ForeignKey(Prenda, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.prenda)

class PantalonLista(LoginRequiredMixin, ListView):
    model = Prenda
    template_name = '.html'
    
    def get_queryset(self):
        return Prenda.objects.filter(tipo__startswith='pantalon')
