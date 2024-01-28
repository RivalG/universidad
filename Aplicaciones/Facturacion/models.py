from django.db import models

class CarreraRAGP(models.Model):
    idCarreraRAGP = models.AutoField(primary_key=True)
    estudianteRAGP = models.CharField(max_length=100)
    facultad = models.CharField(max_length=100)
    nombreCarreraRAGP = models.CharField(max_length=100)
    directorCarreraRAGP = models.CharField(max_length=100)
    logoCarreraRAGP = models.ImageField(upload_to='logos', null=True, blank=True)

    def __str__(self):
        return self.nombreCarreraRAGP



class CursoRAGP(models.Model):
    idCursoRAGP = models.AutoField(primary_key=True)
    estudianteRAGP = models.ForeignKey(CarreraRAGP, on_delete=models.CASCADE)
    nivelCursoRAGP = models.CharField(max_length=50)
    descripcionCursoRAGP = models.TextField()
    aulaCursoRAGP = models.CharField(max_length=20)
    numeroEstudiantesRAGP = models.IntegerField()

    def __str__(self):
        return self.idCursoRAGP




class AsignaturaRAGP(models.Model):
    idAsignaturaRAGP = models.AutoField(primary_key=True)
    estudianteRAGP = models.ForeignKey(CarreraRAGP, on_delete=models.CASCADE)
    nombreAsignaturaRAGP = models.CharField(max_length=100)
    creditosAsignaturaRAGP = models.PositiveIntegerField()
    fechaInicioAsignaturaRAGP = models.DateField()
    fechaFinalizacionAsignaturaRAGP = models.DateField()
    profesorAsignaturaRAGP = models.CharField(max_length=100)
    silaboAsignaturaRAGP = models.FileField(upload_to='silabos/', null=True, blank=True)
    mandilAsignaturaRAGP = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombreAsignaturaRAGP
