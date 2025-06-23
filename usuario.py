import datetime
from abc import ABC, abstractmethod

class Usuario(ABC):
    """
    Clase abstracta que representa un usuario genérico con nombre, apellido, DNI y fecha de nacimiento.
    """

    def __init__(self, nombre, apellido, dni, fecha_nacimiento):
        """
        Inicializa un nuevo usuario.
        :param nombre: str - nombre del usuario
        :param apellido: str - apellido del usuario
        :param dni: str - documento de identidad
        :param fecha_nacimiento: datetime.date - fecha de nacimiento
        """
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento


    @property
    def nombre(self):
        """Devuelve el nombre del usuario."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Modifica el nombre del usuario."""
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        """Devuelve el apellido del usuario."""
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        """Modifica el apellido del usuario."""
        self._apellido = nuevo_apellido

    @property
    def dni(self):
        """Devuelve el DNI del usuario."""
        return self._dni

    @dni.setter
    def dni(self, nuevo_dni):
        """Modifica el DNI del usuario."""
        self._dni = nuevo_dni

    @property
    def fecha_nacimiento(self):
        """Devuelve la fecha de nacimiento del usuario."""
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha):
        """Modifica la fecha de nacimiento del usuario."""
        self._fecha_nacimiento = nueva_fecha


    def calcular_edad(self):
        """
        Calcula y devuelve la edad del usuario según la fecha actual.
        :return: int - edad en años
        """
        fecha_actual = datetime.date.today()
        edad = fecha_actual.year - self._fecha_nacimiento.year
        if (fecha_actual.month, fecha_actual.day) < (self._fecha_nacimiento.month, self._fecha_nacimiento.day):
            edad -= 1
        return edad

    @abstractmethod
    def mostrar_datos(self):
        """
        Método abstracto que debe ser implementado por clases hijas para mostrar los datos del usuario.
        """
        pass







