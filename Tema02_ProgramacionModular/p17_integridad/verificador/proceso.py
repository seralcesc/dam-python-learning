import os


def es_fichero_valido(ruta):
    return os.path.exists(ruta) and os.path.isfile(ruta)
