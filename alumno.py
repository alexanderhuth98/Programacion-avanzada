from usuario import Usuario
import datetime

class Alumno(Usuario):
    """
    Clase que representa a un alumno, hereda de Usuario.
    """

    def __init__(self, nombre, apellido, dni, fecha_nacimiento, legajo):
        """
        Inicializa un alumno con datos personales y su legajo.
        :param nombre: str
        :param apellido: str
        :param dni: str
        :param fecha_nacimiento: datetime.date
        :param legajo: str
        """
        super().__init__(nombre, apellido, dni, fecha_nacimiento)
        self._legajo = legajo

    @property
    def legajo(self):
        """Devuelve el legajo del alumno."""
        return self._legajo

    @legajo.setter
    def legajo(self, nuevo_legajo):
        """Modifica el legajo del alumno."""
        self._legajo = nuevo_legajo

    def mostrar_datos(self):
        """
        Imprime los datos del alumno: nombre, apellido, DNI, edad y legajo.
        """
        print(f"Alumno: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni} | Edad: {self.calcular_edad()}")
        print(f"Legajo: {self.legajo}")

    @classmethod
    def eliminar(cls, lista_alumnos, dni_a_eliminar):
        """
        Elimina un alumno de una lista a partir del DNI.
        :param lista_alumnos: list - lista de alumnos
        :param dni_a_eliminar: str - DNI del alumno a eliminar
        """
        for alumno in lista_alumnos:
            if alumno.dni == dni_a_eliminar:
                lista_alumnos.remove(alumno)
                print(f"Alumno con DNI '{dni_a_eliminar}' fue eliminado.")
                return
        print(f"No se encontró un alumno con DNI '{dni_a_eliminar}'.")


    def to_dict(self):
        """
        Serializa el objeto alumno en un diccionario para su almacenamiento.
        :return: dict
        """
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "fecha_nacimiento": self.fecha_nacimiento.isoformat(),
            "legajo": self.legajo
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Alumno desde un diccionario.
        :param data: dict - datos del alumno
        :return: Alumno
        """
        fecha = datetime.date.fromisoformat(data["fecha_nacimiento"])
        return cls(data["nombre"], data["apellido"], data["dni"], fecha, data["legajo"])
