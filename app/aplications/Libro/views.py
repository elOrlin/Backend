from rest_framework.generics import ListAPIView

from .models import Autor, Libro

from .serializers import AutorSerializer, LibroSerializer


class ListaAutores(ListAPIView):

    serializer_class = AutorSerializer

    def get_queryset(self):
        queryset = Autor.objects.listar_autores_pais('Dominicana')
        return queryset


class FiltroAutores(ListAPIView):

    serializer_class = AutorSerializer

    def get_queryset(self):
        edad = self.kwargs['edad']
        country = self.kwargs['pais']
        print(edad, country)
        queryset = Autor.objects.listar_autores_pais(edad, country)
        return queryset


class LibrosPosteriores(ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        queryset = Autor.objects.listar_libros_posteriores(year)
        return queryset


class LibrosPorTitulo(ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', 'j')
        queryset = Libro.objects.libros_por_titulo(kword)
        return queryset

