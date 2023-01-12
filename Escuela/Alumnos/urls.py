from django.urls import path
from Alumnos.views import create_alumno, list_alumno

urlpatterns = [
    path('create_alumno/',create_alumno),
    path('list_alumno/', list_alumno)
]