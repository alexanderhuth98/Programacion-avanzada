import json
import os

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)

def cargar_json(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)
