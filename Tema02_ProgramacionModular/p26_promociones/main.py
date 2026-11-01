from tienda import ofertas, calendario_promos
import datetime


if __name__ == "__main__":
    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    print("=== TICKET DE VENTA COMERCIAL ===")
    precio = float(input("Precio original del artículo (€): "))
    print("[SISTEMA] Evaluando campaña del mes actual...")

    mes_actual = datetime.datetime.now().month
    nombre_mes = meses[mes_actual - 1]

    if calendario_promos.es_mes_promocional(mes_actual):
        print(f"¡Descuento promocional de {nombre_mes} aplicado!")
        precio_descuento = ofertas.aplicar_rebaja_temporada(precio)
        print(f"Precio final a cobrar: {precio_descuento:.2f} €")
    else:
        print("No hay promociones para este mes.")
        print(f"Precio final a cobrar: {precio:.2f} €")
