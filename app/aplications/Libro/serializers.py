from rest_framework import serializers, pagination

from .models import Autor, Libro


class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 50

class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = [
            'name',
            'last_name',
            'country'
        ]

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = [
            'title',
            'autor',
            'date'
        ]