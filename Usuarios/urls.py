from django.urls import path

from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('landing_admin/<int:usuario_id>/', views.menu, name='landing_admin'),

    path('cursos_admin/<int:usuario_id>/', views.cursos_admin, name='cursos_admin'),
    path('evaluaciones_admin/<int:usuario_id>/', views.evaluaciones_admin, name='evaluaciones_admin'),
    path('evaluadores_admin/<int:usuario_id>/', views.evaluadores_admin, name='evaluadores_admin'),
    path('rubricas_admin/<int:usuario_id>/', views.rubricas_admin, name='rubricas_admin'),

    ##para registrarse
    path('registro/', views.registro, name='registro'),
]