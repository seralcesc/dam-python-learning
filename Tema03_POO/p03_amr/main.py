# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       22/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 3: Robot AMR Logística Automatizada
# Descripción: 2 Paquetes: robotica / navegacion
#
# Gestionar la batería de un robot móvil autónomo (AMR) y calcular la
# distancia máxima en metros que puede recorrer en planta.
# ============================================================


import sys

from navegacion.autonomia import CalculadorAutonomia
from robotica.amr import RobotAMR


def ejecutar_aplicacion():
    print("=== AUTONOMÍA ROBOT AMR LOGÍSTICA ===")
    if len(sys.argv) == 2:
        pct_bateria = float(sys.argv[1])
    else:
        pct_bateria = float(input("Porcentaje de batería (%): "))

    robot = RobotAMR("AMR-LOG-04", pct_bateria)
    autonomia = CalculadorAutonomia()
    distancia = autonomia.estimar_distancia_m(robot.bateria_pct)

    print("-------------------------------------------")
    print(
        f"🤖 Robot {robot.id_robot} | Carga: {robot.bateria_pct}% | Autonomía estimada: {distancia:.2f} metros"
    )


if __name__ == "__main__":
    ejecutar_aplicacion()
