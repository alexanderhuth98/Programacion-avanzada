from usuario import Usuario
import datetime

class Profesor(Usuario):
    """
    Clase que representa a un profesor, hereda de Usuario y contiene una lista de materias que dicta.
    """
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, materias_dictadas):
        """
        Inicializa un profesor con sus datos personales y materias que dicta.
        :param nombre: str
        :param apellido: str
        :param dni: str
        :param fecha_nacimiento: datetime.date
        :param materias_dictadas: list[str]
        """
        super().__init__(nombre, apellido, dni, fecha_nacimiento)
        self.materias_dictadas = materias_dictadas

    def mostrar_datos(self):
        """
        Muestra por consola los datos del profesor, incluyendo las materias que dicta.
        """
        print(f"Profesor: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni} | Edad: {self.calcular_edad()}")
        print("Materias dictadas:")
        for materia in self.materias_dictadas:
            print(f" - {materia}")

    @classmethod
    def eliminar(cls, lista_profesores, dni_a_eliminar):
        """
        Elimina un profesor de la lista según su DNI.
        :param lista_profesores: list - lista de profesores
        :param dni_a_eliminar: str - DNI del profesor a eliminar
        """
        for prof in lista_profesores:
            if prof.dni == dni_a_eliminar:
                lista_profesores.remove(prof)
                print(f"Profesor con DNI '{dni_a_eliminar}' fue eliminado.")
                return
        print(f"No se encontró un profesor con DNI '{dni_a_eliminar}'.")



    def to_dict(self):
        """
        Serializa el objeto profesor a un diccionario para su almacenamiento.
        :return: dict
        """
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "fecha_nacimiento": self.fecha_nacimiento.isoformat(),
            "materias_dictadas": self.materias_dictadas
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Profesor a partir de un diccionario.
        :param data: dict
        :return: Profesor
        """
        fecha = datetime.date.fromisoformat(data["fecha_nacimiento"])
        return cls(data["nombre"], data["apellido"], data["dni"], fecha, data["materias_dictadas"])
