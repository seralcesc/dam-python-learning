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

from diagnostico.analizador import AnalizadorVibracion
from iiot.vibracion import SensorVibracion


def ejecutar_aplicacion():
    print("=== MONITOR IIOT VIBRACIÓN ISO 10816 ===")

    if len(sys.argv) == 3:
        id_motor = sys.argv[1]
        vibracion = float(sys.argv[2])
    else:
        id_motor = input("Introduce ID del Motor Industrial: ")
        vibracion = float(input("Introduce lectura de Vibración RMS (mm/s): "))

    sensor = SensorVibracion(id_motor, vibracion)
    analizador = AnalizadorVibracion()
    estado = analizador.evaluar_estado(sensor)

    print("-------------------------------------------")
    print(
        f"⚙️ [MOTOR {sensor.id_motor}] RMS: {sensor._vibracion_rms} mm/s | Estado Diadnóstico: {estado}"
    )


if __name__ == "__main__":
    ejecutar_aplicacion()
