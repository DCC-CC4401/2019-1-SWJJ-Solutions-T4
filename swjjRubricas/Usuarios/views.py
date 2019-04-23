from django.shortcuts import render


def login(request):
    return render(request, 'Usuarios/login.html')

def menu(request):
    return render(request, 'Usuarios/menu.html')