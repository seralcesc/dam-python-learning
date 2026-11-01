
import parking.tarifas as tarifas
import parking.ticket as ticket

if __name__ == "__main__":
    minutos = int(input("¿Cuántos minutos desea estacionar?: "))
    importe = tarifas.calcular_precio_estancia(minutos)
    importe_formateado = ticket.formatear_moneda(importe)
    fecha_hora_actual = ticket.obtener_hora_actual()

    print("\n--- PARQUÍMETRO MUNICIPAL ---")
    print(f"¿Cuántos minutos desea estacionar?: {minutos}")
    print("-----------------------------------")
    print("TICKET DE ESTACIONAMIENTO ZONA AZUL")
    print(f"Fecha y hora de emisión: {fecha_hora_actual}")
    print(f"Tiempo abonado: {minutos} minutos")
    print(f"IMPORTE TOTAL: {importe_formateado}")
    print("-----------------------------------")