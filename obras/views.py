from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Obras
from django.db.models import Q

def inicio(request):
    obras = Obras.objects.all()
    valor_buscado=request.GET.get("buscador") or ''
    mensaje = ''
    if valor_buscado:
        obras = Obras.objects.filter(
            Q(nombre__icontains = valor_buscado)
        ).distinct()
        if not obras.exists():
            mensaje = "El producto que busca no se encuentra, escriba otro"

    tablas= Obras.objects.prefetch_related('imagenes').all()
    for t in tablas:
        print(f"Obra: {t.nombre}")
        print(f"Descripción: {t.descripcion}")
        print("Imágenes:")
        for imagen in t.imagenes.all():
            print(imagen.imagen.url)

    return render(request, 'obras/inicio.html', {'obras': obras, 'mensaje': mensaje, 'valor_buscado': valor_buscado})



def detalle(request, obra_id):
    obra = get_object_or_404(Obras, pk=obra_id)
    return render(request, 'obras/detalle.html', {'obra': obra})

def autor(request):
    return render(request, 'obras/autor.html')
