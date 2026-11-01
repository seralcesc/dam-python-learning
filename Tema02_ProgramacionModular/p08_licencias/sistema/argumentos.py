import sys


def obtener_clave_desde_cli():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return ""