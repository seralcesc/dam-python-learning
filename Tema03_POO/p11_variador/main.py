# ============================================================
# Autor:        Sergio Alcántara
# Fecha:        25/11/2026
# Archivo:      main.py
# Ejercicio:    Proyecto 11: Conversor de Frecuencia Estático (Hz a RPM)
# Descripción:  2 Paquetes: unidades / variadores
#
# Convertir la frecuencia en Hz entregada por un variador de velocidad a
# revoluciones por minuto (RPM) usando un método estático.
# ============================================================

import sys

from unidades.frecuencia import FrecuenciaMotor
from variadores.calculo import ConversorVariador


def ejecutar_aplicacion():
    print("=== CALCULADORA VARIADOR DE FRECUENCIA ===")
    if len(sys.argv) == 3:
        hz = float(sys.argv[1])
        num_pares_polos = int(sys.argv[2])
    else:
        hz = float(input("Frecuencia consignada en variador (Hz): "))
        num_pares_polos = int(input("Pares de polos del motor asíncrono: "))

    print("-------------------------------------------")

    fm1 = FrecuenciaMotor(hz)
    hz = fm1.hz
    rpm = ConversorVariador.hz_a_rpm(fm1.hz, num_pares_polos)
    print(f"🔄 Conversión Variador: {hz} = {rpm:.2f} RPM")


if __name__ == "__main__":
    ejecutar_aplicacion()
