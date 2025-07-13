from rest_framework.generics import ListAPIView

from .models import Autor, Libro

from .serializers import AutorSerializer, LibroSerializer, PaginationSerializer


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
        kword = self.request.query_params.get('kword', '')
        queryset = Libro.objects.libros_por_titulo(kword)
        return queryset


class FiltrarLibros(ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        year = self.request.query_params.get('year', 1990)
        queryset = Libro.objects.filtrar_libros(kword, year)
        return queryset


class LibroAutor(ListAPIView):
    serializer_class = LibroSerializer
    pagination_class = PaginationSerializer

    def get_queryset(self):
        autor = self.request.query_params.get('autor__name', "")
        queryset = Libro.objects.por_autor(autor)
        return queryset
