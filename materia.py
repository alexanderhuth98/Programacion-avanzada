from profesor import Profesor

class Materia:
    def __init__(self, nombre, profesor=None):
        self._nombre = nombre
        self._profesor = profesor  
        self._alumnos = []         


    @property
    def nombre(self):
        return self._nombre

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, nuevo_profesor):
        if isinstance(nuevo_profesor, Profesor):
            self._profesor = nuevo_profesor


    def agregar_alumno(self, alumno):
        self._alumnos.append(alumno)

    def listar_alumnos(self):
        print(f"Alumnos inscriptos en {self.nombre}:")
        if self._alumnos:
            for a in self._alumnos:
                print(f" - {a.nombre} {a.apellido}")
        else:
            print(" - No hay alumnos inscriptos.")


    def mostrar_datos(self):
        print(f"Materia: {self.nombre}")
        if self.profesor:
            print(f"Profesor/a: {self.profesor.nombre} {self.profesor.apellido}")
        else:
            print("Profesor/a: No asignado")
        self.listar_alumnos()

    
    @classmethod
    def eliminar(cls, lista_materias, nombre_a_eliminar):
        for materia in lista_materias:
            if materia.nombre == nombre_a_eliminar:
                lista_materias.remove(materia)
                print(f"Materia '{nombre_a_eliminar}' eliminada.")
                return
        print(f"No se encontró una materia con nombre '{nombre_a_eliminar}'.")