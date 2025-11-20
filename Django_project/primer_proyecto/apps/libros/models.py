from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(null=True, blank=True)
    isnb = models.CharField(max_length=13, unique=True)
    disponible = models.BooleanField(default=True)
    categoria = models.CharField(max_length=100, default="Sin categoria")

    def __str__(self):
        return f"{self.titulo} - {self.autor}"