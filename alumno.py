from usuario import Usuario

class Alumno(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, legajo):
        super().__init__(nombre, apellido, dni, fecha_nacimiento)
        self._legajo = legajo

    @property
    def legajo(self):
        return self._legajo

    @legajo.setter
    def legajo(self, nuevo_legajo):
        self._legajo = nuevo_legajo

    def mostrar_datos(self):
        print(f"Alumno: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni} | Edad: {self.calcular_edad()}")
        print(f"Legajo: {self.legajo}")

    @classmethod
    def eliminar(cls, lista_alumnos, dni_a_eliminar):
        for alumno in lista_alumnos:
            if alumno.dni == dni_a_eliminar:
                lista_alumnos.remove(alumno)
                print(f"Alumno con DNI '{dni_a_eliminar}' fue eliminado.")
                return
        print(f"No se encontró un alumno con DNI '{dni_a_eliminar}'.")
