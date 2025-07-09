from rest_framework import serializers

from .models import Autor, Libro

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