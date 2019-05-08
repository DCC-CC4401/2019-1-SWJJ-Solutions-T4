from django.db import models


# Create your models here.

class Rubrica(models.Model):
    nombre: object = models.CharField(max_length=100)
    duracion_minima = models.TimeField(u"Duración Mínima")
    duracion_maxima = models.TimeField(u"Duración Máxima")


class Criterio(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)


class Puntaje(models.Model):
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)
    texto = models.CharField(max_length=250)
