from django.contrib import admin

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplications.Libro.urls'), name='libros_app'),
    path('', include('aplications.Prestamo.urls'), name='prestamos_app')
]
