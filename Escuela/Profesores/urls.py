from django.urls import path
from Profesores.views import create_profesor, list_profesor

urlpatterns = [
    path('create_profesor/',create_profesor),
    path('list_profesor/', list_profesor)
]