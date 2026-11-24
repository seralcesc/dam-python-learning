# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       24/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 6: Control de Acceso Ciberseguridad OT
# Descripción: 1 Paquete: ciberseguridad
#
# Bloquear la consola SCADA de una subestación si se introducen 3 claves
# criptográficas erróneas seguidas.
# =======================================================

import sys

from ciberseguridad.terminal import TerminalSCADA


def ejecutar_aplicacion():
    print("=== CONSOLA CIBERSEGURIDAD SCADA OT ===")
    if len(sys.argv) == 2:
        token_probado = sys.argv[1]
    else:
        token_probado = input(
            "Introduce Token de Acceso para el Terminal HMI:"
        )

    t1 = TerminalSCADA("HMI-SUBESTACION", "TOKEN-INVALIDO-01")
    valido = t1.validar_acceso(token_probado)

    print("-------------------------------------------")

    if valido:
        print(f"🔒 [ACCESO CONCEDIDO SCADA] | Terminal: {t1.id_terminal}")

    else:
        print(
            f"🔒 [ACCESO DENEGADO SCADA] Intentos fallidos: {t1.intentos_fallidos}/3 | Terminal: {t1.id_terminal}"
        )


if __name__ == "__main__":
    ejecutar_aplicacion()
