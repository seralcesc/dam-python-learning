# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       19/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 1: IIoT Sensor Vibración Motor Industrial
# Descripción: 2 Paquetes: iiot / diagnostico
# Capturar lecturas de aceleración en mm/s en motores de alta potencia para
# determinar el riesgo de desalineación o fallo mecánico.
# ============================================================
import sys

from iiot.vibracion import SensorVibracion
from iiot.diagnostico.analizador import AnalizadorVibracion


def ejecutar_aplicacion():
    print("=== MONITOR IIOT VIBRACION ISO 10816 ===")
