from django.shortcuts import render

# tal vez deba borrar algunas de estas
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
##

# formularios
from .forms import RegistroUsuarioForm, RegistroEvaluadorForm
from .forms import NuevoCurso
##
from .models import Usuario_admin, Course, Rubrica, Criterio, Puntaje, Usuario_evaluador
import csv


def login(request):
    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('password')

        # Verificar si es admin
        if (Usuario_admin.objects.filter(name=username, password=password).exists()):
            user = Usuario_admin.objects.get(name=username, password=password)
            return HttpResponseRedirect(reverse('usuarios:landing_admin', kwargs={'usuario_id': user.id}))

        if (Usuario_evaluador.objects.filter(correo=username, password=password).exists()):
            user = Usuario_evaluador.objects.get(correo=username, password=password)
            return HttpResponseRedirect(reverse('usuarios:evaluaciones_admin', kwargs={'usuario_id': user.id}))


    return render(request, 'Usuarios/login.html')


def courses(request):
    listaCursos = Course.objects.all()
    return listaCursos


def menu(request, usuario_id):
    # aca deberia haccerse la autenticaciondel usuario.
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    return render(request, 'Usuarios/Admin/Landing_admin.html', {'usuario': usuario})


def cursos_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    if request.POST:
        form = NuevoCurso(request.POST, request.FILES)
        if form.is_valid():  # si no no crea los cleaned data
            form.save()

    listaCursos = courses(request)
    form = NuevoCurso()

    # le paso el form, nuevo_curso a la página.
    return render(request, 'Usuarios/Admin/Cursos_admin.html',
                  {'usuario': usuario, 'nuevo_curso': form, 'listaCursos': listaCursos})


def evaluaciones_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Evaluaciones_admin.html', {'usuario': usuario})


def evaluaciones_admin_ver(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Evaluaciones_admin_ver.html', {'usuario': usuario})

def evaluadoresReq(request):
    listaEvaluadores = Usuario_evaluador.objects.all()
    return listaEvaluadores


def evaluadores_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    if request.POST:
        form = RegistroEvaluadorForm(request.POST, request.FILES)
        if form.is_valid():  # si no no crea los cleaned data
            form.save(usuario_id) # por el override, ver forms

    listaEvaluadores = evaluadoresReq(request)
    form = RegistroEvaluadorForm()

    # le paso el form, nuevo_curso a la página.
    return render(request, 'Usuarios/Admin/Evaluadores_admin.html', {'usuario': usuario, 'nuevo_eval' : form,
                                                                     'listaEval' : listaEvaluadores})


# Commit 15.05
def rubricas_admin(request, usuario_id):
    listaDeRubricas = Rubrica.objects.all()  # Sobre el se itera
    coleccionDeCriterios = []  # Se enviará al html
    nombresRubricas = []  # Se enviará al html

    for rubrica in listaDeRubricas:
        nombresRubricas.append(rubrica.nombre)  # toString?
        with open(rubrica.dataTable) as datosDeLaRubrica:
            buffer = csv.reader(datosDeLaRubrica, delimiter=';')  # Se lee en un formato dado, excel lo separo por ;
            criterios = []  # Una nueva lista de criterios

            iterableBuffer = list(
                buffer)  # Evitar este error:
            # https://stackoverflow.com/questions/32038776/csv-reader-object-is-not-subscriptable

            slicedBuffer = iterableBuffer[2:]  # Se quitan los titulos y el tiempo asociado
            for row in slicedBuffer:
                criterios.append(row[0])  # Se agrega el nombre del criterio
            coleccionDeCriterios.append(criterios)  # Se agrega el criterio

    iterableListForHTML = []
    for i in range(len(listaDeRubricas)):
        l = []
        l.append(nombresRubricas[i])
        l.append(coleccionDeCriterios[i])
        l.append(i)
        iterableListForHTML.append(l)

    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Rubricas_admin.html',
                  {'usuario': usuario, 'listaConRubricas': iterableListForHTML})


def rubricas_admin_create(request, usuario_id):
    # Esta es
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Rubricas_admin_create.html', {'usuario': usuario})


# para el registro
def registro(request):
    if request.POST:
        form = RegistroUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            new_admin = form.save()

            return HttpResponseRedirect(reverse('usuarios:landing_admin', kwargs={'usuario_id': new_admin.id}))

    form = RegistroUsuarioForm()

    return render(request, 'Usuarios/registro/Registro.html', {'register_form': form})
