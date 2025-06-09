import datetime
from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento

    # ---- Propiedades (getters/setters) ----
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, nuevo_dni):
        self._dni = nuevo_dni

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha):
        self._fecha_nacimiento = nueva_fecha


    def calcular_edad(self):
        fecha_actual = datetime.date.today()
        edad = fecha_actual.year - self._fecha_nacimiento.year
        if (fecha_actual.month, fecha_actual.day) < (self._fecha_nacimiento.month, self._fecha_nacimiento.day):
            edad -= 1
        return edad

    @abstractmethod
    def mostrar_datos(self):
        pass





