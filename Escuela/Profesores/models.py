from django.db import models

class Profesores(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Materia = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
