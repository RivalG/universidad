from django.shortcuts import render, redirect
from .models import CarreraRAGP, CursoRAGP, AsignaturaRAGP
from django.contrib import messages
from datetime import datetime

def listadoCarreras(request):
    carreras = CarreraRAGP.objects.all()
    return render(request, 'carreras.html', {'carreras': carreras})

def guardarCarrera(request):
    if request.method == 'POST':
        nombreCarreraRAGP = request.POST.get('nombreCarreraRAGP')
        estudianteRAGP = request.POST.get('estudianteRAGP')
        facultad = request.POST.get('facultad')
        directorCarreraRAGP = request.POST.get('directorCarreraRAGP')
        logoCarreraRAGP = request.FILES.get('logoCarreraRAGP')

        if nombreCarreraRAGP and estudianteRAGP and facultad and directorCarreraRAGP:
            CarreraRAGP.objects.create(
                nombreCarreraRAGP=nombreCarreraRAGP,
                estudianteRAGP=estudianteRAGP,
                facultad=facultad,
                directorCarreraRAGP=directorCarreraRAGP,
                logoCarreraRAGP=logoCarreraRAGP
            )
            messages.success(request, 'Carrera guardada exitosamente.')
            return redirect('listadoCarreras')
        else:
            messages.error(request, 'Error al guardar la carrera. Por favor, complete los campos obligatorios.')

    return render(request, 'carrera.html')

def editarCarrera(request, idCarreraRAGP):
    carrera = CarreraRAGP.objects.get(idCarreraRAGP=idCarreraRAGP)

    if request.method == 'POST':
        nombreCarreraRAGP = request.POST.get('nombreCarreraRAGP')
        estudianteRAGP = request.POST.get('estudianteRAGP')
        facultad = request.POST.get('facultad')
        directorCarreraRAGP = request.POST.get('directorCarreraRAGP')
        logoCarreraRAGP = request.FILES.get('logoCarreraRAGP')

        if nombreCarreraRAGP and estudianteRAGP and facultad and directorCarreraRAGP:
            carrera.nombreCarreraRAGP = nombreCarreraRAGP
            carrera.estudianteRAGP = estudianteRAGP
            carrera.facultad = facultad
            carrera.directorCarreraRAGP = directorCarreraRAGP
            if logoCarreraRAGP:
                carrera.logoCarreraRAGP = logoCarreraRAGP
            carrera.save()
            messages.success(request, 'Carrera editada exitosamente.')
            return redirect('listadoCarreras')
        else:
            messages.error(request, 'Error al editar la carrera. Por favor, complete los campos obligatorios.')

    return render(request, 'editarCarrera.html', {'carrera': carrera})

def actualizarCarrera(request, idCarreraRAGP):
    carrera = CarreraRAGP.objects.get(idCarreraRAGP=idCarreraRAGP)

    if request.method == 'POST':
        nombreCarreraRAGP = request.POST.get('nombreCarreraRAGP')
        estudianteRAGP = request.POST.get('estudianteRAGP')
        facultad = request.POST.get('facultad')
        directorCarreraRAGP = request.POST.get('directorCarreraRAGP')
        logoCarreraRAGP = request.FILES.get('logoCarreraRAGP')

        if nombreCarreraRAGP and estudianteRAGP and facultad and directorCarreraRAGP:
            carrera.nombreCarreraRAGP = nombreCarreraRAGP
            carrera.estudianteRAGP = estudianteRAGP
            carrera.facultad = facultad
            carrera.directorCarreraRAGP = directorCarreraRAGP
            if logoCarreraRAGP:
                carrera.logoCarreraRAGP = logoCarreraRAGP
            carrera.save()
            messages.success(request, 'Carrera actualizada exitosamente.')
            return redirect('listadoCarreras')
        else:
            messages.error(request, 'Error al actualizar la carrera. Por favor, complete los campos obligatorios.')

    return render(request, 'editarCarrera.html', {'carrera': carrera})


def eliminarCarrera(request, idCarreraRAGP):
    try:
        carrera = CarreraRAGP.objects.get(idCarreraRAGP=idCarreraRAGP)
        carrera.delete()
        messages.success(request, 'Carrera eliminada exitosamente.')
    except CarreraRAGP.DoesNotExist:
        messages.error(request, 'La carrera que intenta eliminar no existe.')

    return redirect('listadoCarreras')

#--------------------------------------------------CURSO----------------------------------------------------------------------
def listarCursos(request):
    cursos = CursoRAGP.objects.all()
    carreras = CarreraRAGP.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos, 'carreras': carreras})

def guardarCurso(request):
    if request.method == 'POST':
        estudianteRAGP_id = request.POST.get('estudianteRAGP')
        nivelCursoRAGP = request.POST.get('nivelCursoRAGP')
        descripcionCursoRAGP = request.POST.get('descripcionCursoRAGP')
        aulaCursoRAGP = request.POST.get('aulaCursoRAGP')
        numeroEstudiantesRAGP = request.POST.get('numeroEstudiantesRAGP')

        if estudianteRAGP_id and nivelCursoRAGP and descripcionCursoRAGP and aulaCursoRAGP and numeroEstudiantesRAGP:
            CursoRAGP.objects.create(
                estudianteRAGP_id=estudianteRAGP_id,
                nivelCursoRAGP=nivelCursoRAGP,
                descripcionCursoRAGP=descripcionCursoRAGP,
                aulaCursoRAGP=aulaCursoRAGP,
                numeroEstudiantesRAGP=numeroEstudiantesRAGP
            )
            messages.success(request, 'Curso guardado exitosamente.')
            return redirect('listarCursos')
        else:
            messages.error(request, 'Error al guardar el curso. Por favor, complete los campos obligatorios.')

    return render(request, 'cursos.html')

def editarCurso(request, idCursoRAGP):
    curso = CursoRAGP.objects.get(idCursoRAGP=idCursoRAGP)
    carreras = CarreraRAGP.objects.all()
    return render(request, 'editarCurso.html', {'curso': curso, 'carreras': carreras})


    if request.method == 'POST':
        idCursoRAGP = request.POST.get('idCursoRAGP')
        estudianteRAGP_id = request.POST.get('estudianteRAGP_id')
        nivelCursoRAGP = request.POST.get('nivelCursoRAGP')
        descripcionCursoRAGP = request.POST.get('descripcionCursoRAGP')
        aulaCursoRAGP = request.POST.get('aulaCursoRAGP')
        numeroEstudiantesRAGP = request.POST.get('numeroEstudiantesRAGP')

        if idCursoRAGP and estudianteRAGP_id and nivelCursoRAGP and descripcionCursoRAGP and aulaCursoRAGP and numeroEstudiantesRAGP:
            curso.idCursoRAGP = idCursoRAGP
            curso.estudianteRAGP_id = estudianteRAGP_id
            curso.nivelCursoRAGP = nivelCursoRAGP
            curso.descripcionCursoRAGP = descripcionCursoRAGP
            curso.aulaCursoRAGP = aulaCursoRAGP
            curso.numeroEstudiantesRAGP = numeroEstudiantesRAGP
            curso.save()
            messages.success(request, 'Curso editado exitosamente.')
            return redirect('listadoCursos')
        else:
            messages.error(request, 'Error al editar el curso. Por favor, complete los campos obligatorios.')

    return render(request, 'editarCurso.html', {'curso': curso})

def eliminarCurso(request, idCursoRAGP):
    try:
        curso = CursoRAGP.objects.get(idCursoRAGP=idCursoRAGP)
        curso.delete()
        messages.success(request, 'Curso eliminado exitosamente.')
    except CursoRAGP.DoesNotExist:
        messages.error(request, 'El curso que intenta eliminar no existe.')

    return redirect('listadoCursos')


def actualizarCurso(request, idCursoRAGP):
    curso = CursoRAGP.objects.get(idCursoRAGP=idCursoRAGP)

    if request.method == 'POST':
        estudianteRAGP_id = request.POST["estudianteRAGP"]
        nivelCursoRAGP = request.POST["nivelCursoRAGP"]
        descripcionCursoRAGP = request.POST["descripcionCursoRAGP"]
        aulaCursoRAGP = request.POST["aulaCursoRAGP"]
        numeroEstudiantesRAGP = request.POST["numeroEstudiantesRAGP"]

        # Validar que los campos obligatorios no estén vacíos
        if not estudianteRAGP_id or not nivelCursoRAGP or not descripcionCursoRAGP or not aulaCursoRAGP or not numeroEstudiantesRAGP:
            messages.error(request, 'Error al actualizar el curso. Por favor, complete los campos obligatorios.')
            return redirect('listarCursos')

        # Actualizar el objeto CursoRAGP
        curso.estudianteRAGP_id = estudianteRAGP_id
        curso.nivelCursoRAGP = nivelCursoRAGP
        curso.descripcionCursoRAGP = descripcionCursoRAGP
        curso.aulaCursoRAGP = aulaCursoRAGP
        curso.numeroEstudiantesRAGP = numeroEstudiantesRAGP
        curso.save()

        messages.success(request, 'Curso actualizado exitosamente.')
        return redirect('listarCursos')

    return render(request, 'editarCurso.html', {'curso': curso, 'carreras': CarreraRAGP.objects.all()})





#------------------------------------------------------ASIGNATURA-------------------------------------------------------------------

def listadoAsignaturas(request):
    asignaturas = AsignaturaRAGP.objects.all()
    carreras = CarreraRAGP.objects.all()
    return render(request, 'asignaturas.html', {'asignaturas': asignaturas, 'carreras': carreras})


def guardarAsignatura(request):
    if request.method == 'POST':
        estudianteRAGP_id = request.POST.get('estudianteRAGP')
        nombreAsignaturaRAGP = request.POST.get('nombreAsignaturaRAGP')
        creditosAsignaturaRAGP = request.POST.get('creditosAsignaturaRAGP')
        fechaInicioAsignaturaRAGP = request.POST.get('fechaInicioAsignaturaRAGP')
        fechaFinalizacionAsignaturaRAGP = request.POST.get('fechaFinalizacionAsignaturaRAGP')
        profesorAsignaturaRAGP = request.POST.get('profesorAsignaturaRAGP')
        silaboAsignaturaRAGP = request.FILES.get('silaboAsignaturaRAGP')
        mandilAsignaturaRAGP = request.POST.get('mandilAsignaturaRAGP')

        if estudianteRAGP_id and nombreAsignaturaRAGP and creditosAsignaturaRAGP and fechaInicioAsignaturaRAGP and fechaFinalizacionAsignaturaRAGP and profesorAsignaturaRAGP:
            # Convertir las fechas de cadena a objetos de fecha
            fecha_inicio = datetime.strptime(fechaInicioAsignaturaRAGP, '%Y-%m-%d').date()
            fecha_finalizacion = datetime.strptime(fechaFinalizacionAsignaturaRAGP, '%Y-%m-%d').date()

            AsignaturaRAGP.objects.create(
                estudianteRAGP_id=estudianteRAGP_id,
                nombreAsignaturaRAGP=nombreAsignaturaRAGP,
                creditosAsignaturaRAGP=creditosAsignaturaRAGP,
                fechaInicioAsignaturaRAGP=fecha_inicio,
                fechaFinalizacionAsignaturaRAGP=fecha_finalizacion,
                profesorAsignaturaRAGP=profesorAsignaturaRAGP,
                silaboAsignaturaRAGP=silaboAsignaturaRAGP,
                mandilAsignaturaRAGP=mandilAsignaturaRAGP
            )
            messages.success(request, 'Asignatura guardada exitosamente.')
            return redirect('listadoAsignaturas')
        else:
            messages.error(request, 'Error al guardar la asignatura. Por favor, complete los campos obligatorios.')

    return render(request, 'asignaturas.html')


def editarAsignatura(request, idAsignaturaRAGP):
    asignatura = AsignaturaRAGP.objects.get(idAsignaturaRAGP=idAsignaturaRAGP)
    carreras = CarreraRAGP.objects.all()

    if request.method == 'POST':
        idAsignaturaRAGP = request.POST.get('idAsignaturaRAGP')
        estudianteRAGP_id = request.POST.get('estudianteRAGP_id')
        nombreAsignaturaRAGP = request.POST.get('nombreAsignaturaRAGP')
        creditosAsignaturaRAGP = request.POST.get('creditosAsignaturaRAGP')
        fechaInicioAsignaturaRAGP = request.POST.get('fechaInicioAsignaturaRAGP')
        fechaFinalizacionAsignaturaRAGP = request.POST.get('fechaFinalizacionAsignaturaRAGP')
        profesorAsignaturaRAGP = request.POST.get('profesorAsignaturaRAGP')
        silaboAsignaturaRAGP = request.FILES.get('silaboAsignaturaRAGP')
        mandilAsignaturaRAGP = request.POST.get('mandilAsignaturaRAGP')

        if idAsignaturaRAGP and estudianteRAGP_id and nombreAsignaturaRAGP and creditosAsignaturaRAGP and fechaInicioAsignaturaRAGP and fechaFinalizacionAsignaturaRAGP and profesorAsignaturaRAGP:
            asignatura.idAsignaturaRAGP = idAsignaturaRAGP
            asignatura.estudianteRAGP_id = estudianteRAGP_id
            asignatura.nombreAsignaturaRAGP = nombreAsignaturaRAGP
            asignatura.creditosAsignaturaRAGP = creditosAsignaturaRAGP
            asignatura.fechaInicioAsignaturaRAGP = fechaInicioAsignaturaRAGP
            asignatura.fechaFinalizacionAsignaturaRAGP = fechaFinalizacionAsignaturaRAGP
            asignatura.profesorAsignaturaRAGP = profesorAsignaturaRAGP
            if silaboAsignaturaRAGP:
                asignatura.silaboAsignaturaRAGP = silaboAsignaturaRAGP
            asignatura.mandilAsignaturaRAGP = mandilAsignaturaRAGP
            asignatura.save()
            messages.success(request, 'Asignatura editada exitosamente.')
            return redirect('listadoAsignaturas')
        else:
            messages.error(request, 'Error al editar la asignatura. Por favor, complete los campos obligatorios.')

    return render(request, 'editarAsignatura.html', {'asignatura': asignatura, 'carreras': carreras})


def eliminarAsignatura(request, idAsignaturaRAGP):
    try:
        asignatura = AsignaturaRAGP.objects.get(idAsignaturaRAGP=idAsignaturaRAGP)
        asignatura.delete()
        messages.success(request, 'Asignatura eliminada exitosamente.')
    except AsignaturaRAGP.DoesNotExist:
        messages.error(request, 'La asignatura que intenta eliminar no existe.')

    return redirect('listadoAsignaturas')


def actualizarAsignatura(request, idAsignaturaRAGP):
    asignatura = AsignaturaRAGP.objects.get(idAsignaturaRAGP=idAsignaturaRAGP)

    if request.method == 'POST':
        estudianteRAGP_id = request.POST.get('estudianteRAGP')
        nombreAsignaturaRAGP = request.POST.get('nombreAsignaturaRAGP')
        creditosAsignaturaRAGP = request.POST.get('creditosAsignaturaRAGP')
        fechaInicioAsignaturaRAGP = request.POST.get('fechaInicioAsignaturaRAGP')
        fechaFinalizacionAsignaturaRAGP = request.POST.get('fechaFinalizacionAsignaturaRAGP')
        profesorAsignaturaRAGP = request.POST.get('profesorAsignaturaRAGP')
        silaboAsignaturaRAGP = request.FILES.get('silaboAsignaturaRAGP')
        mandilAsignaturaRAGP = request.POST.get('mandilAsignaturaRAGP')

        # Validar que los campos obligatorios no estén vacíos
        if not estudianteRAGP_id or not nombreAsignaturaRAGP or not creditosAsignaturaRAGP or not fechaInicioAsignaturaRAGP or not fechaFinalizacionAsignaturaRAGP or not profesorAsignaturaRAGP:
            messages.error(request, 'Error al actualizar la asignatura. Por favor, complete los campos obligatorios.')
            return redirect('listadoAsignaturas')

        # Formatear fechas
        try:
            fechaInicio = datetime.strptime(fechaInicioAsignaturaRAGP, "%Y-%m-%d").date()
            fechaFinalizacion = datetime.strptime(fechaFinalizacionAsignaturaRAGP, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, 'Fecha inválida. Formato esperado: YYYY-MM-DD')
            return redirect('listadoAsignaturas')

        # Actualizar el objeto AsignaturaRAGP
        asignatura.estudianteRAGP_id = estudianteRAGP_id
        asignatura.nombreAsignaturaRAGP = nombreAsignaturaRAGP
        asignatura.creditosAsignaturaRAGP = creditosAsignaturaRAGP
        asignatura.fechaInicioAsignaturaRAGP = fechaInicio
        asignatura.fechaFinalizacionAsignaturaRAGP = fechaFinalizacion
        asignatura.profesorAsignaturaRAGP = profesorAsignaturaRAGP
        asignatura.mandilAsignaturaRAGP = mandilAsignaturaRAGP

        if silaboAsignaturaRAGP:
            asignatura.silaboAsignaturaRAGP = silaboAsignaturaRAGP

        asignatura.save()

        messages.success(request, 'Asignatura actualizada exitosamente.')

        # Redirigir a 'listadoAsignaturas' después de guardar
        return redirect('listadoAsignaturas')

    return render(request, 'editarAsignatura.html', {'asignatura': asignatura})
