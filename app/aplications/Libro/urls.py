from django.urls import path, register_converter

from .views import ListaAutores, FiltroAutores, LibrosPosteriores, LibrosPorTitulo
from . import converters

app_name = "libros_app"


register_converter(converters.TwoDigits, 'nn')
register_converter(converters.validYearConverter, 'aaaa')

urlpatterns = [
    path('api/autor/list/', ListaAutores.as_view()),
    path('api/autor/filtro/<nn:edad>/<pais>/', FiltroAutores.as_view()),
    path('api/libro/posteriores/<aaaa:year>/', LibrosPosteriores.as_view()),
    path('api/libro/por-titulo/', LibrosPorTitulo.as_view())

]