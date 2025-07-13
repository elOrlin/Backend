from django.db import models


class AutorManager(models.Manager):

    def listar_autores_pais(self, pais, edad):
        return self.filter(
            country=pais,
            edad__lte=edad
        )


class LibroManager(models.Manager):

    def listar_libros_posteriores(self, year):
        return self.filter(
            date__year__gt=year
        )

    def libros_por_titulo(self, kword):
        return self.filter(
            title__icontains=kword
        ).order_by('title')

    def filtrar_libros(self, kword, year):
        return self.filter(
            title__icontains=kword,
            date__year__gt=year
        )

    def por_autor(self, autor_name):
        return self.filter(
            autor__name__icontains=autor_name
        ).order_by('date')