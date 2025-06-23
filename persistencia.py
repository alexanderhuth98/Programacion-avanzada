import json
import os

def guardar_json(nombre_archivo, datos):
    """
    Guarda datos serializados en formato JSON en un archivo.

    :param nombre_archivo: str - nombre del archivo donde se guardará
    :param datos: list|dict - datos a guardar
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)

def cargar_json(nombre_archivo):
    """
    Carga datos desde un archivo JSON. Si el archivo no existe, devuelve una lista vacía.

    :param nombre_archivo: str - nombre del archivo desde el cual se cargará
    :return: list|dict - datos cargados
    """
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)
