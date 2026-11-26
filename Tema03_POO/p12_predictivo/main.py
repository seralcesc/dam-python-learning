# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       26/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 12: Mantenimiento Predictivo Trazas
# Descripción: 1 Paquete: mantenimiento
#
# Generar incidencias técnicas con IDs secuenciales usando atributos d
# clase e imprimiendo la marca de tiempo de datetime.
# ============================================================

import sys

from mantenimiento.incidencia import IncidenciaTecnica


def ejecutar_aplicacion():
    print("=== ORDEN DE MANTENIMIENTO PREDICTIVO ===")
    if len(sys.argv) == 2:
        maquina = sys.argv[1]
    else:
        maquina = input("Nombre de la máquina afectada: ")

    print("-------------------------------------------")

    it = IncidenciaTecnica(maquina)
    print(it.obtener_traza_mantenimiento())


if __name__ == "__main__":
    ejecutar_aplicacion()
