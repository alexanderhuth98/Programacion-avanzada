from profesor import Profesor

class Materia:
    """
    Clase que representa una materia, con un profesor asignado y una lista de alumnos inscriptos.
    """
    def __init__(self, nombre, profesor=None):
        """
        Inicializa una materia con un nombre y un profesor opcional.
        :param nombre: str
        :param profesor: Profesor (opcional)
        """
        self._nombre = nombre
        self._profesor = profesor  
        self._alumnos = []         


    @property
    def nombre(self):
        """Devuelve el nombre de la materia."""
        return self._nombre

    @property
    def profesor(self):
        """Devuelve el profesor asignado a la materia."""
        return self._profesor

    @profesor.setter
    def profesor(self, nuevo_profesor):
        """Asigna un nuevo profesor a la materia si es instancia de Profesor."""
        if isinstance(nuevo_profesor, Profesor):
            self._profesor = nuevo_profesor


    def agregar_alumno(self, alumno):
        """Agrega un alumno a la lista de alumnos inscriptos."""
        self._alumnos.append(alumno)

    def listar_alumnos(self):
        """Imprime la lista de alumnos inscriptos en la materia."""
        print(f"Alumnos inscriptos en {self.nombre}:")
        if self._alumnos:
            for a in self._alumnos:
                print(f" - {a.nombre} {a.apellido}")
        else:
            print(" - No hay alumnos inscriptos.")


    def mostrar_datos(self):
        """Imprime los datos de la materia, incluyendo profesor y alumnos."""
        print(f"Materia: {self.nombre}")
        if self.profesor:
            print(f"Profesor/a: {self.profesor.nombre} {self.profesor.apellido}")
        else:
            print("Profesor/a: No asignado")
        self.listar_alumnos()

    
    @classmethod
    def eliminar(cls, lista_materias, nombre_a_eliminar):
        """
        Elimina una materia de una lista por nombre.
        :param lista_materias: list - lista de materias
        :param nombre_a_eliminar: str - nombre de la materia a eliminar
        """
        for materia in lista_materias:
            if materia.nombre == nombre_a_eliminar:
                lista_materias.remove(materia)
                print(f"Materia '{nombre_a_eliminar}' eliminada.")
                return
        print(f"No se encontró una materia con nombre '{nombre_a_eliminar}'.")



    def to_dict(self):
        """
        Serializa la materia a un diccionario, usando DNI para profesor y alumnos.
        :return: dict
        """
        return {
            "nombre": self.nombre,
            "profesor_dni": self.profesor.dni if self.profesor else None,
            "alumnos_dni": [a.dni for a in self._alumnos]
        }

    @classmethod
    def from_dict(cls, data, lista_profesores, lista_alumnos):
        """
        Crea una instancia de Materia desde un diccionario, relacionando profesor y alumnos por DNI.
        :param data: dict
        :param lista_profesores: list
        :param lista_alumnos: list
        :return: Materia
        """
        profesor = next((p for p in lista_profesores if p.dni == data["profesor_dni"]), None)
        materia = cls(data["nombre"], profesor)
        for dni in data["alumnos_dni"]:
            alumno = next((a for a in lista_alumnos if a.dni == dni), None)
            if alumno:
                materia.agregar_alumno(alumno)
        return materia
