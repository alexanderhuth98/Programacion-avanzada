import datetime
from alumno import Alumno
from profesor import Profesor
from materia import Materia
from persistencia import guardar_json, cargar_json


lista_alumnos = [Alumno.from_dict(a) for a in cargar_json("alumnos.json")]
lista_profesores = [Profesor.from_dict(p) for p in cargar_json("profesores.json")]
lista_materias = [Materia.from_dict(m, lista_profesores, lista_alumnos) for m in cargar_json("materias.json")]


def input_fecha():
    """Solicita una fecha de nacimiento al usuario y la devuelve como objeto date."""
    while True:
        try:
            fecha_str = input("Fecha de nacimiento (YYYY-MM-DD): ")
            return datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            print("Formato inválido.")


def guardar_todo():
    """Guarda todas las listas en sus respectivos archivos JSON."""
    guardar_json("alumnos.json", [a.to_dict() for a in lista_alumnos])
    guardar_json("profesores.json", [p.to_dict() for p in lista_profesores])
    guardar_json("materias.json", [m.to_dict() for m in lista_materias])


def alta_alumno():
    """Crea un nuevo alumno y lo agrega a la lista."""
    print("\n--- Alta de Alumno ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    fecha_nac = input_fecha()
    legajo = input("Legajo: ")
    alumno = Alumno(nombre, apellido, dni, fecha_nac, legajo)
    lista_alumnos.append(alumno)
    guardar_todo()
    print("Alumno agregado.")

def baja_alumno():
    """Elimina un alumno de la lista a partir del DNI."""
    dni = input("DNI del alumno a eliminar: ")
    Alumno.eliminar(lista_alumnos, dni)
    guardar_todo()

def modificar_alumno():
    """Modifica los datos de un alumno ya existente."""
    dni = input("DNI del alumno a modificar: ")
    for a in lista_alumnos:
        if a.dni == dni:
            a.nombre = input(f"Nuevo nombre [{a.nombre}]: ") or a.nombre
            a.apellido = input(f"Nuevo apellido [{a.apellido}]: ") or a.apellido
            a.legajo = input(f"Nuevo legajo [{a.legajo}]: ") or a.legajo
            guardar_todo()
            print("Alumno modificado.")
            return
    print("Alumno no encontrado.")

def listar_alumnos():
    """Lista todos los alumnos registrados."""
    if lista_alumnos:
        for a in lista_alumnos:
            a.mostrar_datos()
    else:
        print("No hay alumnos cargados.")


def alta_profesor():
    """Crea un nuevo profesor y lo agrega a la lista."""
    print("\n--- Alta de Profesor ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    fecha_nac = input_fecha()
    materias = input("Materias que dicta (separadas por coma): ").split(",")
    materias = [m.strip() for m in materias if m.strip()]
    profesor = Profesor(nombre, apellido, dni, fecha_nac, materias)
    lista_profesores.append(profesor)
    guardar_todo()
    print("Profesor agregado.")

def baja_profesor():
    """Elimina un profesor de la lista a partir del DNI."""
    dni = input("DNI del profesor a eliminar: ")
    Profesor.eliminar(lista_profesores, dni)
    guardar_todo()

def modificar_profesor():
    """Modifica los datos de un profesor ya existente."""
    dni = input("DNI del profesor a modificar: ")
    for p in lista_profesores:
        if p.dni == dni:
            p.nombre = input(f"Nuevo nombre [{p.nombre}]: ") or p.nombre
            p.apellido = input(f"Nuevo apellido [{p.apellido}]: ") or p.apellido
            nuevas_materias = input("Nuevas materias dictadas (separadas por coma): ")
            if nuevas_materias:
                p.materias_dictadas = [m.strip() for m in nuevas_materias.split(",")]
            guardar_todo()
            print("Profesor modificado.")
            return
    print("Profesor no encontrado.")

def listar_profesores():
    """Lista todos los alumnos registrados."""
    if lista_profesores:
        for p in lista_profesores:
            p.mostrar_datos()
    else:
        print("No hay profesores cargados.")


def alta_materia():
    """Crea una nueva materia y lo agrega a la lista."""
    print("\n--- Alta de Materia ---")
    nombre = input("Nombre de la materia: ")
    
    if not lista_profesores:
        print("Debe haber al menos un profesor.")
        return
    
    print("Profesores disponibles:")
    for i, p in enumerate(lista_profesores):
        print(f"{i+1}. {p.nombre} {p.apellido}")
    try:
        profesor = lista_profesores[int(input("Seleccioná un profesor (número): ")) - 1]
    except (IndexError, ValueError):
        print("Selección inválida.")
        return

    materia = Materia(nombre, profesor)

    if lista_alumnos:
        print("Alumnos disponibles:")
        for i, a in enumerate(lista_alumnos):
            print(f"{i+1}. {a.nombre} {a.apellido}")
        indices = input("Seleccioná alumnos (ej: 1,2,3): ").split(",")
        for i in indices:
            try:
                alumno = lista_alumnos[int(i.strip()) - 1]
                materia.agregar_alumno(alumno)
            except (IndexError, ValueError):
                continue

    lista_materias.append(materia)
    guardar_todo()
    print("Materia agregada.")

def baja_materia():
    """Elimina una materia de la lista a partir del nombre."""
    nombre = input("Nombre de la materia a eliminar: ")
    Materia.eliminar(lista_materias, nombre)
    guardar_todo()

def modificar_materia():
    """Modifica los datos de una materia ya existente."""
    nombre = input("Nombre de la materia a modificar: ")
    for m in lista_materias:
        if m.nombre == nombre:
            print("1. Cambiar profesor")
            print("2. Agregar alumno")
            opcion = input("Opción: ")
            if opcion == "1":
                for i, p in enumerate(lista_profesores):
                    print(f"{i+1}. {p.nombre} {p.apellido}")
                try:
                    m.profesor = lista_profesores[int(input("Nuevo profesor (número): ")) - 1]
                    guardar_todo()
                    print("Profesor cambiado.")
                except (IndexError, ValueError):
                    print("Selección inválida.")
            elif opcion == "2":
                for i, a in enumerate(lista_alumnos):
                    print(f"{i+1}. {a.nombre} {a.apellido}")
                try:
                    m.agregar_alumno(lista_alumnos[int(input("Alumno a agregar (número): ")) - 1])
                    guardar_todo()
                    print("Alumno agregado.")
                except (IndexError, ValueError):
                    print("Selección inválida.")
            return
    print("Materia no encontrada.")

def listar_materias():
    """Lista todos las materias registradas."""
    if lista_materias:
        for m in lista_materias:
            m.mostrar_datos()
    else:
        print("No hay materias cargadas.")

# ---------------------------------------------------------------------------- Menú principal --------------------------------------------------------------------------
def menu():
    """Muestra el menú principal del sistema y delega a submenús."""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. ABM Alumnos")
        print("2. ABM Profesores")
        print("3. ABM Materias")
        print("0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            submenu_abm("Alumno", alta_alumno, baja_alumno, modificar_alumno, listar_alumnos)
        elif opcion == "2":
            submenu_abm("Profesor", alta_profesor, baja_profesor, modificar_profesor, listar_profesores)
        elif opcion == "3":
            submenu_abm("Materia", alta_materia, baja_materia, modificar_materia, listar_materias)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

def submenu_abm(nombre, alta, baja, modificar, listar):
    """Submenú genérico para las operaciones de ABM."""
    while True:
        print(f"\n--- ABM {nombre.upper()} ---")
        print("1. Alta")
        print("2. Baja")
        print("3. Modificación")
        print("4. Listar")
        print("0. Volver")
        opcion = input("Opción: ")
        if opcion == "1":
            alta()
        elif opcion == "2":
            baja()
        elif opcion == "3":
            modificar()
        elif opcion == "4":
            listar()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu()
