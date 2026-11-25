# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       25/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 8: Brazo Robótico Servomotores
# Descripción: 1 Paquete: cinematica
#
# Evaluar la posición angular de los servomotores de un robot articulado
# e identificar si se encuentra en zona de colisión.
# =======================================================


import sys

from cinematica.articulacion import ServoArticulacion


def ejecutar_aplicacion():
    print("=== CONTROL CINEMÁTICO ROBÓTICA ===")
    if len(sys.argv) == 3:
        id_eje = sys.argv[1]
        angulo_grados = float(sys.argv[2])
    else:
        id_eje = input("Identificador del Eje de la Articulación: ")
        angulo_grados = float(input("Ángulo servomotor asignado (º): "))

    print("-------------------------------------------")

    sa1 = ServoArticulacion(id_eje, angulo_grados)
    eje = sa1.id_eje
    grados = sa1.angulo_grados
    estado = sa1.obtener_zona_trabajo()

    print(f"🦾 [ARTICULACIÓN {eje}] Ángulo: {grados}º | Estado: {estado}")


if __name__ == "__main__":
    ejecutar_aplicacion()
