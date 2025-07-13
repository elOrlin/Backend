from django.db import models


class prestamoManager(models.Manager):

    def listar_por_fecha(self, fecha):
        return self.filter(
            date__lte=fecha
        )
