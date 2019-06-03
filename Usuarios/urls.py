from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('landing_admin/<int:usuario_id>/', views.menu, name='landing_admin'),

    path('cursos_admin/<int:usuario_id>/', views.cursos_admin, name='cursos_admin'),

    path('cursos_admin_create/<int:usuario_id>/<int:id_curso>/', views.cursos_admin_create, name='cursos_admin_create'),
    path('cursos_admin_delete/<int:usuario_id>/<int:id_curso>/', views.cursos_admin_delete, name='cursos_admin_delete'),

    path('evaluaciones_admin/<int:usuario_id>/', views.evaluaciones_admin, name='evaluaciones_admin'),
    path('evaluaciones_admin_ver/<int:usuario_id>/', views.evaluaciones_admin_ver, name='evaluaciones_admin_ver'),
    path('evaluaciones_admin_create/<int:usuario_id>/', views.evaluaciones_admin_create, name='evaluaciones_admin_create'),
    path('evaluadores_admin/<int:usuario_id>/', views.evaluadores_admin, name='evaluadores_admin'),

    path('evaluadores_admin_edit/<int:usuario_id>/<int:eval_id>/', views.evaluadores_admin_edit, name='evaluadores_admin_edit'),
    path('evaluadores_admin_delete/<int:usuario_id>/<int:eval_id>/', views.evaluadores_admin_delete, name='evaluadores_admin_delete'),

    path('rubricas_admin/<int:usuario_id>/', views.rubricas_admin, name='rubricas_admin'),
    path('rubricas_admin_create/<int:usuario_id>/', views.rubricas_admin_create, name='rubricas_admin_create'),

    # para registrarse
    path('registro/', views.registro, name='registro'),
]
