from django.db import models


# Create your models here.

class Rubrica(models.Model):
    nombre: object = models.CharField(max_length=100)
    duracion_minima = models.TimeField(u"Duración Mínima")
    duracion_maxima = models.TimeField(u"Duración Máxima")

    def __str__(self):
        return self.nombre

    def getCriterios(self):
        '''
        Gets all criterios of this rubrica
        :return: a list of Criterio
        '''
        return Criterio.objects.filter(rubrica__nombre=self.nombre)


class Criterio(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def getPuntajes(self):
        '''
        Gets all puntaje that belong to this criterio
        :return: a list of Puntaje
        '''
        return Puntaje.objects.filters(criterio__nombre=self.nombre)


class Puntaje(models.Model):
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto
