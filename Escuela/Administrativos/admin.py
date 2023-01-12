from django.contrib import admin

from Administrativos.models import Administrativos
from Alumnos.models import Alumnos
from Profesores.models import Profesores

@admin.register(Administrativos)
class AdministrativosAdmin(admin.ModelAdmin):
    list_display = ('name','age','activo')
    list_filter = ('age','activo')
    search_fields = ('name',)

@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('name','age','activo')
    list_filter = ('age','activo')
    search_fields = ('name',)

@admin.register(Profesores)
class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ('name','age','activo')
    list_filter = ('age','Materia')
    search_fields = ('name',)