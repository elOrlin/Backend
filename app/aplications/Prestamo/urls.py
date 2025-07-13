from django.urls import path

from .views import prestamoList

app_name = "prestamos_app"

urlpatterns = [
    path('prestamo/', prestamoList.as_view())
]
