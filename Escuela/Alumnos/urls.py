from django.urls import path
from Alumnos.views import create_alumno, list_alumno,update_alumno, AlumnosListViews,AlumnosDeleteView

urlpatterns = [
    path('create_alumno/',create_alumno),
    path('list_alumno/', list_alumno),
    path('update_alumno/<int:pk>/',update_alumno),
    path('delete_alumno/<int:pk>/',AlumnosDeleteView.as_view())
]