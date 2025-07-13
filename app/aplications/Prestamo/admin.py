from django.contrib import admin

from .models import Estudiante, Prestamo, Devolucion


# Register your models here.
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name'
    )


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'description',
        'student',
        'date'
    )


@admin.register(Devolucion)
class DevolucionAdmin(admin.ModelAdmin):
    list_display = (
        'loan',
        'date'
    )
