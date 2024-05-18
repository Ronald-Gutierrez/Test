from django.urls import path
from .views import inicio, detalle, autor

urlpatterns = [
    path('', inicio, name='inicio'),
    path('detalle/<int:obra_id>/', detalle, name='detalle'),
    path('autor', autor, name='autor'),
]