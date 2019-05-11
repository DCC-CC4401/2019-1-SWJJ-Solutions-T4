from django.shortcuts import render

##talvez deba borrar algunas de estas
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
##

##formularios
from .forms import RegistroUsuarioForm
from .forms import NuevoCurso
##
from .models import Usuario_admin


def login(request):
    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('password')

        user = Usuario_admin.objects.get(name=username, password=password)

        if user is not None:
            return HttpResponseRedirect(reverse('usuarios:landing_admin', kwargs={'usuario_id': user.id}))

    return render(request, 'Usuarios/login.html')


def menu(request, usuario_id):
    # aca deberia haccerse la autenticaciondel usuario.
    usuario = Usuario_admin.objects.get(pk=usuario_id)

    return render(request, 'Usuarios/Admin/Landing_admin.html', {'usuario': usuario})


def cursos_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)


    if request.POST:
        form = NuevoCurso(request.POST, request.FILES)
        if form.is_valid():
            form.save()


    form = NuevoCurso()



    ##le paso el form, nuevo_curso a la pagina.
    return render(request, 'Usuarios/Admin/Cursos_admin.html', {'usuario': usuario,'nuevo_curso': form})


def evaluaciones_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Evaluaciones_admin.html', {'usuario': usuario})


def evaluadores_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Evaluadores_admin.html', {'usuario': usuario})


def rubricas_admin(request, usuario_id):
    usuario = Usuario_admin.objects.get(pk=usuario_id)
    return render(request, 'Usuarios/Admin/Rubricas_admin.html', {'usuario': usuario})


# para el registro
def registro(request):
    if request.POST:
        form = RegistroUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            new_admin = form.save()

            return HttpResponseRedirect(reverse('usuarios:landing_admin', kwargs={'usuario_id': new_admin.id}))

    form = RegistroUsuarioForm()

    return render(request, 'Usuarios/registro/Registro.html', {'register_form': form})
