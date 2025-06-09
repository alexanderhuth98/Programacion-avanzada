import datetime
from alumno import Alumno
from profesor import Profesor
from materia import Materia


profesor1 = Profesor(
    nombre="Lucía",
    apellido="Fernández",
    dni="45678901",
    fecha_nacimiento=datetime.date(1985, 2, 14),
    materias_dictadas=["Matemática", "Física"]
)

alumno1 = Alumno(
    nombre="Carlos",
    apellido="Pérez",
    dni="40234567",
    fecha_nacimiento=datetime.date(2003, 6, 10),
    legajo="A1234"
)

alumno2 = Alumno(
    nombre="Ana",
    apellido="López",
    dni="40345678",
    fecha_nacimiento=datetime.date(2004, 3, 15),
    legajo="A5678"
)


materia1 = Materia(nombre="Matemática", profesor=profesor1)
materia1.agregar_alumno(alumno1)
materia1.agregar_alumno(alumno2)


print("profesor 1:")
profesor1.mostrar_datos()
print("\n alumno 1:")
alumno1.mostrar_datos()
print("\n alumno 2:")
alumno2.mostrar_datos()
print("\n materia:")
materia1.mostrar_datos()


lista_profesores = [profesor1]
lista_alumnos = [alumno1, alumno2]
lista_materias = [materia1]

Profesor.eliminar(lista_profesores, "45678901")
Alumno.eliminar(lista_alumnos, "40345678")
Materia.eliminar(lista_materias, "Matemática")

# luego de eliminar
print("\n lista de profesores actualizada")
for p in lista_profesores:
    p.mostrar_datos()


print("\n lista de alumnos actualizada")
for a in lista_alumnos:
    a.mostrar_datos()


print("\n lista de materias actualizada")
for m in lista_materias:
    m.mostrar_datos()
