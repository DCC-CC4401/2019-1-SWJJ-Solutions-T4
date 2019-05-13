from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Usuario_admin(models.Model):
    name = models.CharField(max_length=200)
    app_paterno = models.CharField(max_length=50, blank=True, null=True)
    app_materno = models.CharField(max_length=50, blank=True, null=True)
    isAdmin = models.BooleanField(default=True)
    password = models.CharField(max_length=50)


class Course(models.Model):
    nombreCurso = models.CharField(max_length=250, help_text='Nombre del curso ')
    codigoCurso = models.CharField(max_length=8, help_text='Codigo curso ')
    numSeccionCurso = models.IntegerField(help_text='Numero seccion del curso')
    anioCurso = models.IntegerField(help_text='Año del curso ')
    semesterCurso = models.IntegerField(help_text='Semestre ')

    def __str__(self):
        return self.nombreCurso


class Rubrica(models.Model):
    nombre: object = models.CharField(max_length=100)
    duracion_minima = models.TimeField(u"Duración Mínima")
    duracion_maxima = models.TimeField(u"Duración Máxima")

    def __str__(self):
        return self.nombre

    def get_criterios(self):
        """
        Gets all criterios of this rubrica
        :return: a list of Criterio
        """
        return Criterio.objects.filter(rubrica__nombre=self.nombre)


class Criterio(models.Model):
    rubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def get_puntajes(self):
        """
        Gets all puntaje that belong to this criterio
        :return: a list of Puntaje
        """
        return Puntaje.objects.filters(criterio__nombre=self.nombre)


class Puntaje(models.Model):
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    puntaje = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto
