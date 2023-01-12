from django.urls import path
from Administrativos.views import create_administrativo, list_administrativo

urlpatterns = [
    path('create_administrativo/',create_administrativo),
    path('list_administrativo/', list_administrativo)
]