from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Usuario_admin, Alumno, Grupo, Usuario_evaluador
from .models import Course
from .models import Rubrica
from .models import Criterio
from .models import Puntaje

admin.site.register(Usuario_admin)
admin.site.register(Course)
admin.site.register(Rubrica)
admin.site.register(Criterio)
admin.site.register(Puntaje)
admin.site.register(Alumno)
admin.site.register(Grupo)
admin.site.register(Usuario_evaluador)