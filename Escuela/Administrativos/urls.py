from django.urls import path
from Administrativos.views import create_administrativo, list_administrativo,update_administrativo,AdministrativoDeleteView

urlpatterns = [
    path('create_administrativo/',create_administrativo),
    path('list_administrativo/', list_administrativo),
    path('update_administrativo/', update_administrativo),
    path('delete_administrativo/<int:pk>/',AdministrativoDeleteView.as_view())
]