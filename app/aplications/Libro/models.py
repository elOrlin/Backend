from django.db import models

from .managers import AutorManager, LibroManager


# Create your models here.
class Autor(models.Model):
    name = models.CharField("Nombre", max_length=20)
    last_name = models.CharField("Apellidos", max_length=20)
    country = models.CharField("Pais", max_length=30)

    objects = AutorManager()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Editorial(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return self.name


class Libro(models.Model):
    title = models.CharField(max_length=30)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    front = models.ImageField('Portada',
                              upload_to='libro', blank=True, null=True)

    objects = LibroManager()

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.title
