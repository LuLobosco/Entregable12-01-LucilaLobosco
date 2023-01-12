from django.db import models

class Administrativos(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name
