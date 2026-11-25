# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       25/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 10: Telemetría Presión Neumática
# Descripción: 1 Paquete: presion
#
# Almacenar presiones barométricas de un circuito de aire comprimido en una
# lista privada y calcular la media mediante statistics.mean.
# =======================================================

import sys

from presion.manometro import ManometroDigital


def ejecutar_aplicacion():
    print("=== TELEMETRÍA DE RED NEUMÁTICA ===")
    if len(sys.argv) == 5:
        circuito = sys.argv[1]
        valor_bar_1 = float(sys.argv[2])
        valor_bar_2 = float(sys.argv[3])
        valor_bar_3 = float(sys.argv[4])
    else:
        circuito = input("Nombre del circuito neumático: ")
        valor_bar_1 = float(input("Presión muestra 1 (bar): "))
        valor_bar_2 = float(input("Presión muestra 2 (bar): "))
        valor_bar_3 = float(input("Presión muestra 3 (bar): "))

    print("-------------------------------------------")

    manometro1 = ManometroDigital(circuito)

    manometro1.agregar_presion(valor_bar_1)
    manometro1.agregar_presion(valor_bar_2)
    manometro1.agregar_presion(valor_bar_3)

    media = manometro1.calcular_media_bar()
    longitud = len(manometro1.presiones_bar)

    print(
        f"🎈 {manometro1.circuito} | {longitud} Muestras | Presión media: {media:.2f} bar"
    )


if __name__ == "__main__":
    ejecutar_aplicacion()
