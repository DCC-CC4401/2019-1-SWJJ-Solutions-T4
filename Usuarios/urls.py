from django.urls import path

from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('landing_admin/', views.menu, name='landing_admin'),

    path('cursos_admin/', views.cursos_admin, name='cursos_admin'),
    path('evaluaciones_admin/', views.evaluaciones_admin, name='evaluaciones_admin'),
    path('evaluadores_admin/', views.evaluadores_admin, name='evaluadores_admin'),
    path('rubricas_admin/', views.rubricas_admin, name='rubricas_admin'),
]