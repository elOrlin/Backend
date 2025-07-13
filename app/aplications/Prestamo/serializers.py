from .models import Prestamo

from rest_framework import serializers


class prestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = [
            'book',
            'description',
            'student',
            'date',
        ]
