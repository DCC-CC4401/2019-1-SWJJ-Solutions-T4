from django.shortcuts import render


def login(request):
    return render(request, 'Usuarios/login.html')

def menu(request):
    return render(request, 'Usuarios/Admin/landingAdmin.html')

def cursos_admin(request):
    return render(request, 'Usuarios/Admin/Admin_interface/Cursos_admin.html')
def evaluaciones_admin(request):
    return render(request, 'Usuarios/Admin/Admin_interface/Cursos_admin.html')
def evaluadores_admin(request):
    return render(request, 'Usuarios/Admin/Admin_interface/Cursos_admin.html')
def rubricas_admin(request):
    return render(request, 'Usuarios/Admin/Admin_interface/Cursos_admin.html')