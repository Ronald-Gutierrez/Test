
from django.db import models
# Create your models here.
class Obras(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='obras/fotos', null=True)


class Imagenes(models.Model):
    obra = models.ForeignKey(Obras, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='obras/fotos')