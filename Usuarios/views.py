from django.shortcuts import render

# tal vez deba borrar algunas de estas
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
##

# formularios
from .forms import RegistroUsuarioForm, RegistroEvaluadorForm, NuevaEvaluacion
from .forms import NuevoCurso
from .forms import NuevoEvaluador
from .forms import NuevaRubrica
##
from .models import Usuario_admin, Course, Rubrica, Criterio, Puntaje, Usuario_evaluador
import csv

##para el json
import json


##
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


def cursos_admin_create(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Cursos_admin_create.html', {'usuario': usuario})


def cursos_admin_delete(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Cursos_admin_delete.html', {'usuario': usuario})


def evaluaciones_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Evaluaciones_admin.html', {'usuario': usuario})


def evaluaciones_admin_ver(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Evaluaciones_admin_ver.html', {'usuario': usuario})


def evaluaciones_admin_create(request, usuario_id):  # TODO: Complete
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    if request.POST:
        form = NuevaEvaluacion(request.POST, request.FILES)
        if form.is_valid():
            # listaDeEvaluadores = form.cleaned_data.get('evaluadores')
            form.save()
    form = NuevaEvaluacion()
    return render(request, 'Usuarios/Admin/Evaluaciones_admin_create.html', {'usuario': usuario, 'nueva_eval': form})


def evaluadoresReq(request):
    listaEvaluadores = Usuario_evaluador.objects.all()
    return listaEvaluadores


def evaluadores_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    if request.POST:
        form = RegistroEvaluadorForm(request.POST, request.FILES)
        if form.is_valid():  # si no no crea los cleaned data
            form.save(usuario_id)  # por el override, ver forms

    listaEvaluadores = evaluadoresReq(request)
    form = RegistroEvaluadorForm()

    # le paso el form, nuevo_curso a la página.
    return render(request, 'Usuarios/Admin/Evaluadores_admin.html', {'usuario': usuario, 'nuevo_eval': form,
                                                                     'listaEval': listaEvaluadores})


# Commit 15.05

def rubricas_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    with open('rubricaJson.json', 'r') as f:
        data = json.load(f)

    rubricsNames = []
    if data:
        for key in data[str(usuario_id)]:
            rubricsNames.append(key)
    print(rubricsNames)

    return render(request, 'Usuarios/Admin/Rubricas_admin.html', {'usuario': usuario, 'rubricsNames': rubricsNames})


def rubricas_admin_create(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    # Esta es
    if request.POST:
        form = NuevaRubrica(request.POST, request.FILES)

        new_rubrica = form.save(request.POST, usuario_id)
        print("rubrica guardada con exito")

    form = NuevaRubrica()

    return render(request, 'Usuarios/Admin/Rubricas_admin_create.html', {'usuario': usuario, 'nueva_rubrica': form})


# para el registro
def registro(request):
    if request.POST:
        form = RegistroUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            new_admin = form.save()

            return HttpResponseRedirect(reverse('usuarios:landing_admin', kwargs={'usuario_id': new_admin.id}))

    form = RegistroUsuarioForm()

    return render(request, 'Usuarios/registro/Registro.html', {'register_form': form})


def rubricas_admin_ver(request, usuario_id, rubricaName):
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    with open('rubricaJson.json') as f:
        data = json.load(f)
    data = data[str(usuario_id)][rubricaName]
    matriz = parseJsonToMatriz(data, int(data.get("numFilas")), int(data.get("numColumnas")))

    return render(request, 'Usuarios/Admin/Rubricas_admin_ver.html',
                  {'usuario': usuario, 'rubrica': data, 'rangei': range(int(data.get("numFilas"))),
                   'rangej': range(int(data.get("numColumnas"))), 'matriz': matriz})


def parseJsonToMatriz(data, numFilas, numColumnas):
    filas = []
    for i in range(numFilas):
        columnas = []
        for j in range(numColumnas):
            s = "f" + str(i) + "c" + str(j)
            columnas.append(data.get(s))

        filas.append(columnas)

    return filas
