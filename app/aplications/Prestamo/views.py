# Create your views here.
from .models import Prestamo

from rest_framework.generics import ListAPIView

from .serializers import prestamoSerializer


class prestamoList(ListAPIView):
    serializer_class = prestamoSerializer

    def get_queryset(self):
        queryset = Prestamo.objects.listar_por_fecha('2025-05-01')
        return queryset
