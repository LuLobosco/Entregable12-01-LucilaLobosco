from django.urls import path
from Profesores.views import create_profesor, list_profesor,ProfesorDeleteView,update_profesor

urlpatterns = [
    path('create_profesor/',create_profesor),
    path('list_profesor/', list_profesor),
    path('update_profesor/<int:pk>/', update_profesor),
    path('delete_profesor/<int:pk>/',ProfesorDeleteView.as_view())
]