# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       23/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 5: Validador de Redundancia PLC Siemens
# Descripción: 2 Paquetes: automatizacion / red
#
# Verificar que la IP configurada en un autómata programable (PLC) pertenezca
# a la subred de control OT 192.168.10.X.
# ============================================================

import sys

from automatizacion.plc import ControladorPLC
from red.seguridad_ot import ValidadorRedOT


def ejecutar_aplicacion():
    print("=== VALIDACIÓN DE AUTOMÁTICAS PLC OT ===")
    if len(sys.argv) == 3:
        id_plc = sys.argv[1]
        ip_control = sys.argv[2]
    else:
        id_plc = input("Identificador del PLC: ")
        ip_control = input("Dirección IP asignada al controlador: ")

    print("-------------------------------------------")
    c1 = ControladorPLC(id_plc, ip_control)
    nombre = c1.id_plc
    direccion = c1.ip_control
    validador = ValidadorRedOT()
    valida = validador.es_ip_valida(direccion)
    if valida:
        print(
            f"📟 [AUTOMATIZACIÓN] Controlador {nombre} validado en subred OT."
        )
    else:
        print(
            f"📟 [AUTOMATIZACIÓN] Controlador {nombre} no validado en subred OT."
        )


if __name__ == "__main__":
    ejecutar_aplicacion()
