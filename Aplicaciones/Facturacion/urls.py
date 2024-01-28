from django.urls import path
from . import views

urlpatterns = [

    # Carreras
    path('', views.listadoCarreras, name='listadoCarreras'),
    path('guardarCarrera/', views.guardarCarrera, name='guardarCarrera'),
    path('editarCarrera/<int:idCarreraRAGP>/', views.editarCarrera, name='editarCarrera'),
    path('actualizarCarrera/<int:idCarreraRAGP>/', views.actualizarCarrera, name='actualizarCarrera'),
    path('eliminarCarrera/<int:idCarreraRAGP>/', views.eliminarCarrera, name='eliminarCarrera'),

    # Cursos
    path('listarCursos/', views.listarCursos, name='listarCursos'),
    path('guardarCurso/', views.guardarCurso, name='guardarCurso'),
    path('editarCurso/<int:idCursoRAGP>/', views.editarCurso, name='editarCurso'),
    path('actualizarCurso/<int:idCursoRAGP>/', views.actualizarCurso, name='actualizarCurso'),
    path('eliminarCurso/<int:idCursoRAGP>/', views.eliminarCurso, name='eliminarCurso'),

    # Asignaturas
    path('listadoAsignaturas/', views.listadoAsignaturas, name='listadoAsignaturas'),
    path('guardarAsignatura/', views.guardarAsignatura, name='guardarAsignatura'),
    path('editarAsignatura/<int:idAsignaturaRAGP>/', views.editarAsignatura, name='editarAsignatura'),
    path('actualizarAsignatura/<int:idAsignaturaRAGP>/', views.actualizarAsignatura, name='actualizarAsignatura'),
    path('eliminarAsignatura/<int:idAsignaturaRAGP>/', views.eliminarAsignatura, name='eliminarAsignatura'),
]
