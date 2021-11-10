

from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        if estudiantes is None:
            self.listadoAlumnos = list()
        else:
            self.listadoAlumnos = estudiantes
        self.asignarNombre()

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas == None:
            self._asignaturas = list()

        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if (lista is None):
            self.listadoAlumnos = [alumno]
        else:
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 12"):
        cls.grado = nombre        

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo