from django.shortcuts import render


def login(request):
    return render(request, 'Usuarios/login.html')


def menu(request):
    return render(request, 'Usuarios/Admin/Landing_admin.html')


def cursos_admin(request):
    return render(request, 'Usuarios/Admin/Cursos_admin.html')


def evaluaciones_admin(request):
    return render(request, 'Usuarios/Admin/Evaluaciones_admin.html')


def evaluadores_admin(request):
    return render(request, 'Usuarios/Admin/Evaluadores_admin.html')


def rubricas_admin(request):
    return render(request, 'Usuarios/Admin/Rubricas_admin.html')
