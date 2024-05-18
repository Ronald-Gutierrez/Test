from django.contrib import admin
from .models import Obras, Imagenes

# Register your models here.

class ImagenProductoAdmin(admin.TabularInline):
    model=Imagenes
class ObrasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'imagen']
    inlines = [
        ImagenProductoAdmin
    ]


admin.site.register(Obras, ObrasAdmin)