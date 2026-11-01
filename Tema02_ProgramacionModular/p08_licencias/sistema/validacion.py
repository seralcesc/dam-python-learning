import sys


def es_clave_correcta(clave):
    return clave == "ADM-1234-OK"

def cerrar_programa_si_error():
    print("Error: Clave incorrecta.")
    sys.exit(1)
