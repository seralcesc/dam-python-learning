# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       22/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 2: Gemelo Digital de Horno de Fundición
# Descripción: 1 Paquete: digital_twin

# Simular la disipación térmica de un horno industrial evitando que la
# temperatura simulada descienda del cero absoluto en Celsius.
# ============================================================

import sys

from digital_twin.horno import GemeloHorno


def ejecutar_aplicacion():
    print("=== SIMULACIÓN GEMELO DIGITAL HORNO ===")
    if len(sys.argv) == 4:
        id_horno = sys.argv[1]
        temp_inicial = float(sys.argv[2])
        minutos = float(sys.argv[3])
    else:
        id_horno = input("ID del Horno de Fundición: ")
        temp_inicial = float(input("Temperatura inicial registrada (ºC): "))
        minutos = float(input("Minutos de purga transcurridos: "))

    horno = GemeloHorno(id_horno, temp_inicial)
    nueva_temp = horno.enfriar(minutos)

    print("-------------------------------------------")
    print(
        f"🔥 [{horno.id_horno}] Temp inicial: {temp_inicial}ºC | Tras {minutos} min purga: {nueva_temp}ºC"
    )


if __name__ == "__main__":
    ejecutar_aplicacion()
