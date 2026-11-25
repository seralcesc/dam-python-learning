# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       24/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 7: Impresora 3D Industrial FDM
# Descripción: 2 Paquetes: fabricacion / tiempo
#
# Calcular la cantidad necesaria de filamento de polímero en fabricacion y
# estimar la hora de finalización en tiempo.
# =======================================================

import sys

from fabricacion.impresora import TrabajoImpresion3D
from tiempo.estimador import EstimadorImpresion


def ejecutar_aplicacion():
    print("=== FABRICACIÓN ADITIVA IMPRESIÓN 3D ===")
    if len(sys.argv) == 3:
        id_pieza = sys.argv[1]
        capas_totales = int(sys.argv[2])
    else:
        id_pieza = input("Identificador de la pieza CAD: ")
        capas_totales = int(input("Número total de capas G-Code: "))

    print("-------------------------------------------")

    i1 = TrabajoImpresion3D(id_pieza, capas_totales)
    material = i1.calcular_material_g()
    estimador = EstimadorImpresion()
    tiempo_estimado = estimador.calcular_tiempo_min(i1)

    print(
        f"🖨️  Pieza {i1.id_pieza} | Material: {material}g filamento | Tiempo estimado: {tiempo_estimado} min"
    )


if __name__ == "__main__":
    ejecutar_aplicacion()
