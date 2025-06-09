from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, materias_dictadas):
        super().__init__(nombre, apellido, dni, fecha_nacimiento)
        self.materias_dictadas = materias_dictadas

    def mostrar_datos(self):
        print(f"Profesor: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni} | Edad: {self.calcular_edad()}")
        print("Materias dictadas:")
        for materia in self.materias_dictadas:
            print(f" - {materia}")

    @classmethod
    def eliminar(cls, lista_profesores, dni_a_eliminar):
        for prof in lista_profesores:
            if prof.dni == dni_a_eliminar:
                lista_profesores.remove(prof)
                print(f"Profesor con DNI '{dni_a_eliminar}' fue eliminado.")
                return
        print(f"No se encontró un profesor con DNI '{dni_a_eliminar}'.")
