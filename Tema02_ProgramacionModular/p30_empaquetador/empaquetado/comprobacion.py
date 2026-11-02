import os


def es_directorio_valido(ruta):
    existe = os.path.exists(ruta)
    es_carpeta = os.path.isdir(existe)
    return existe and es_carpeta
