# ============================================================
# Autor:        Sergio Alcántara
# Fecha:        25/11/2026
# Archivo:      main.py
# Ejercicio:    
# Descripción:  
#
#
# ============================================================

import sys


def ejecutar_aplicacion():
    print("=== TÍTULO ===")
    if len(sys.argv) == 2:
        dato = sys.argv[1]
    else:
        dato = input("Introduce dato: ")

    print("-------------------------------------------")


if __name__ == "__main__":
    ejecutar_aplicacion()
