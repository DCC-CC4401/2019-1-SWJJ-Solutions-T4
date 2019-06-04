from django.shortcuts import render

# tal vez deba borrar algunas de estas
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect # Added
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
            return menu(request,user.id,user.isAdmin)

        if (Usuario_evaluador.objects.filter(correo=username, password=password).exists()):
            user = Usuario_evaluador.objects.get(correo=username, password=password)
            return menu(request,user.id,user.isAdmin)

    return render(request, 'Usuarios/login.html')


def courses(request):
    listaCursos = Course.objects.all()
    return listaCursos


def menu(request, usuario_id,isAdmin):
    # aca deberia haccerse la autenticaciondel usuario.
    if isAdmin==1:
        usuario = Usuario_admin.objects.get(pk=usuario_id)
    else:
        usuario= Usuario_evaluador.objects.get(pk=usuario_id)

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

# TODO : Se encarga de editar o realizar update, ignorar nombre
def cursos_admin_create(request, usuario_id, id_curso):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    curso = Course.objects.get(id=id_curso)
    if request.method == 'GET':
        form = NuevoCurso(instance=curso)
    else:
        form = NuevoCurso(request.POST, request.FILES ,instance=curso)
        if form.is_valid():
            form.save()
        #return redirect('usuarios:cursos_admin', {'usuario' : usuario})
        # SOL : https://stackoverflow.com/questions/13202385/django-reverse-with-arguments-and-keyword-arguments-not-found
        return redirect(reverse('usuarios:cursos_admin',kwargs={'usuario_id' : usuario_id})) # Funciona
    return render(request,'Usuarios/Admin/Cursos_admin_create.html',{'form' : form, 'usuario': usuario, 'curso': curso})

def cursos_admin_delete(request, usuario_id, id_curso):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    curso = Course.objects.get(id = id_curso)
    if request.method == 'POST':
        curso.delete()
        #return redirect('usuarios:cursos_admin')
        return redirect(reverse('usuarios:cursos_admin', kwargs={'usuario_id': usuario_id})) # Funciona
    return render(request, 'Usuarios/Admin/Cursos_admin_delete.html', {'usuario': usuario ,'curso' : curso})

def evaluaciones_admin(request, usuario_id,isAdmin):
    if isAdmin==1:
        usuario = Usuario_admin.objects.get(pk=usuario_id)
    else:
        usuario = Usuario_evaluador.objects.get(pk=usuario_id)



    #esta parte esta harcodeada, pero se deberia arreglar, cuando el modelo Evaluacion este listo
    listaEval = []
    listaEval.append("tarea1")
    listaEval.append("tarea2")




    return render(request, 'Usuarios/Admin/Evaluaciones_admin.html', {'usuario': usuario,'listaEval':listaEval})


def evaluaciones_admin_ver(request, usuario_id,rubrica_name, isAdmin):
    if isAdmin == 1:
        usuario = Usuario_admin.objects.get(pk=usuario_id)
    else:
        usuario = Usuario_evaluador.objects.get(pk=usuario_id)
    with open('rubricaJson.json', 'r') as f:
        data = json.load(f)

    if data:
        if str(usuario_id) in data:
            j=data[str(usuario_id)][rubrica_name]
            matriz = parseJsonToMatriz(j, int(j.get("numFilas")), int(j.get("numColumnas")))
    print(j.get("numColumnas"))
    return render(request, 'Usuarios/Admin/Evaluaciones_admin_ver.html', {'usuario': usuario,'rubrica':j,'matriz':matriz,'rangeCol':range(int(j.get("numColumnas"))-1)})


def evaluaciones_admin_create(request, usuario_id): # TODO: Complete
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
    return render(request, 'Usuarios/Admin/Evaluadores_admin.html', {'usuario': usuario, 'nuevo_evaluador': form,
                                                                     'listaEval': listaEvaluadores})


#def evaluadores_admin_edit(request, usuario_id):
#    usuario = Usuario_admin.objects.get(pk=usuario_id)
#    return render(request, 'Usuarios/Admin/Evaluadores_admin_edit.html', {'usuario': usuario})

def evaluadores_admin_edit(request, usuario_id, eval_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    evaluador = Usuario_evaluador.objects.get(id=eval_id)
    if request.method == 'GET':
        form = RegistroEvaluadorForm(instance=evaluador)
    else:
        form = RegistroEvaluadorForm(request.POST, request.FILES ,instance=evaluador)
        if form.is_valid():
            form.save(usuario_id, evaluador) # Literalmente envia el objeto
        #return redirect('usuarios:cursos_admin', {'usuario' : usuario})
        # SOL : https://stackoverflow.com/questions/13202385/django-reverse-with-arguments-and-keyword-arguments-not-found
        return redirect(reverse('usuarios:evaluadores_admin',kwargs={'usuario_id' : usuario_id})) # Funciona
    return render(request,'Usuarios/Admin/Evaluadores_admin_edit.html',{'form' : form, 'usuario': usuario, 'eval': evaluador})


#def evaluadores_admin_delete(request, usuario_id):
#    usuario = Usuario_admin.objects.get(pk=usuario_id)
#    return render(request, 'Usuarios/Admin/Evaluadores_admin_delete.html', {'usuario': usuario})

def evaluadores_admin_delete(request, usuario_id, eval_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    evaluador = Usuario_evaluador.objects.get(id=eval_id)
    if request.method == 'POST':
        evaluador.delete()
        #return redirect('usuarios:cursos_admin')
        return redirect(reverse('usuarios:evaluadores_admin',kwargs={'usuario_id' : usuario_id})) # Funciona
    return render(request, 'Usuarios/Admin/Evaluadores_admin_delete.html', {'usuario': usuario ,'eval': evaluador})


# Commit 15.05

def rubricas_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    # Primero que nada, guardar una nueva rubrica
    if request.POST:
        form = NuevaRubrica(request.POST, request.FILES)

        new_rubrica = form.save(request.POST, usuario_id)
        print("rubrica guardada con exito")

    with open('rubricaJson.json', 'r') as f:
        data = json.load(f)


    rubricsNames = []
    if data:
        if str(usuario_id) in data:
            for key in data[str(usuario_id)]:
                rubricsNames.append(key)
    print(rubricsNames)

    return render(request, 'Usuarios/Admin/Rubricas_admin.html', {'usuario': usuario, 'rubricsNames': rubricsNames})


def rubricas_admin_create(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    # Esta es
#   Esto ahora se encuentra en rubricas_admin
#    if request.POST:
#        form = NuevaRubrica(request.POST, request.FILES)#
#
#        if form.is_valid():
#           new_rubrica = form.save(request.POST, usuario_id)
#            print("rubrica guardada con exito")
#        else:
#            print("Hay datos incorrectos")
#            return render(request, 'Usuarios/Admin/Rubricas_admin_create.html', {'usuario': usuario, 'nueva_rubrica': form})

    form = NuevaRubrica()

    return render(request, 'Usuarios/Admin/Rubricas_admin_create.html', {'usuario': usuario, 'nueva_rubrica': form})


# para el registro
def registro(request):
    if request.POST:
        form = RegistroUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            new_admin = form.save()
            return menu(request, new_admin.id, new_admin.isAdmin)
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

def rubricas_admin_eliminar(request, usuario_id, rubricaName):
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    with open('rubricaJson.json') as f:
        data = json.load(f)

    del data[str(usuario_id)][rubricaName]

    with open('rubricaJson.json', 'w') as json_file:
        json.dump(data, json_file)

    rubricsNames = []
    if data:
        if str(usuario_id) in data:
            for key in data[str(usuario_id)]:
                rubricsNames.append(key)
    print(rubricsNames)

    return render(request, 'Usuarios/Admin/Rubricas_admin.html', {'usuario': usuario, 'rubricsNames': rubricsNames})




def parseJsonToMatriz(data, numFilas, numColumnas):
    filas = []
    for i in range(numFilas):
        columnas = []
        for j in range(numColumnas):
            s = "f" + str(i) + "c" + str(j)
            columnas.append(data.get(s))

        filas.append(columnas)

    return filas
