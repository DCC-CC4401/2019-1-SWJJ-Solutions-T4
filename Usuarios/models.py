from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Usuario_admin(models.Model):
    name = models.CharField(max_length=200)
    app_paterno = models.CharField(max_length=50, blank=True, null=True)
    app_materno = models.CharField(max_length=50, blank=True, null=True)
    isAdmin = models.BooleanField(default=True)
    password = models.CharField(max_length=50)

class Usuario_evaluador(models.Model):
    name = models.CharField(max_length=200)
    app_paterno = models.CharField(max_length=50, blank=True, null=True)
    app_materno = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    password = models.CharField(max_length=50) # TODO : Remember to randomize
    myAdminID = models.ForeignKey(Usuario_admin,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    nombreCurso = models.CharField(max_length=250, help_text='Nombre del curso ')
    codigoCurso = models.CharField(max_length=8, help_text='Codigo curso ')
    numSeccionCurso = models.IntegerField(help_text='Numero seccion del curso')
    anioCurso = models.IntegerField(help_text='Año del curso ')
    semesterCurso = models.IntegerField(help_text='Semestre ')

    class Meta:
        unique_together = ('codigoCurso', 'numSeccionCurso', 'anioCurso' ,'semesterCurso',)

    def __str__(self):
        return self.nombreCurso

class Grupo(models.Model):
    nombreGrupo = models.CharField(max_length=200)
    cursoGrupo = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreGrupo

class Alumno(models.Model):
    nombreAlumno = models.CharField(max_length=200)
    hasPresented = models.BooleanField(default=False) # Agregado
    grupoAsociado = models.ForeignKey(Grupo,on_delete=models.DO_NOTHING) # TODO: Es buena idea doNothing?
    cursoAsociado = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreAlumno

class Rubrica(models.Model):
    nombre: object = models.CharField(max_length=100)
    duracion_minima = models.TimeField(u"Duración Mínima")
    duracion_maxima = models.TimeField(u"Duración Máxima")
    dataTable = models.FilePathField(path='./RubricasDataTables')


    def __str__(self):
        return self.nombre

    def get_criterios(self):
        """
        Gets all criterios of this rubrica
        :return: a list of Criterio
        """
        return Criterio.objects.filter(rubrica__nombre=self.nombre)

class Evaluacion(models.Model):
    nombre: object = models.CharField(max_length=100)
    curso = models.ForeignKey(Course,on_delete=models.CASCADE)
    equipo = models.ForeignKey(Grupo,on_delete=models.CASCADE) # TODO : Deberia ser do nothing
    rubrica = models.ForeignKey(Rubrica,on_delete=models.CASCADE)
    # evaluadores = models.ManyToManyField(Usuario_evaluador, null=True) # NOT NULL constraint failed

    def __str__(self):
        return self.nombre

class EvaluacionAsignada(models.Model):
    evaluador = models.ManyToManyField(Usuario_evaluador)


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
