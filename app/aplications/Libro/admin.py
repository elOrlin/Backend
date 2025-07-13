from django.contrib import admin
from .models import Autor, Editorial, Libro


# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'country',
    )


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'autor',
        'editorial',
        'date',
       'front'
       )
