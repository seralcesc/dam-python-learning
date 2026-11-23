# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       23/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 4: Medidor Eficiencia Energética Plantas
# Descripción: 1 Paquete: energia
# Calcular el coste económico total del consumo eléctrico de una
# línea de producción aplicando la tarifa por kWh.
# ============================================================

import sys

from energia.contador import MedidorElectrico


def ejecutar_aplicacion():
    print("=== EFICIENCIA ENERGÉTICA INDUSTRIAL ===")
    if len(sys.argv) == 4:
        linea_nom = sys.argv[1]
        kwh_consumidos = float(sys.argv[2])
        tarifa = float(sys.argv[3])
    else:
        linea_nom = input("Nombre de la línea de producción: ")
        kwh_consumidos = float(input("Energía consumida registrada (kwh): "))
        tarifa = float(input("Precio contractual del kwh (€): "))

    print("-------------------------------------------")

    lp1 = MedidorElectrico(linea_nom, kwh_consumidos, tarifa)
    consumo = lp1.kwh_consumidos
    coste = lp1.calcular_coste_total()

    print(
        f"⚡ {lp1.linea_produccion} | Consumo: {consumo} kwh | Coste Energético: {coste}€"
    )


if __name__ == "__main__":
    ejecutar_aplicacion()
