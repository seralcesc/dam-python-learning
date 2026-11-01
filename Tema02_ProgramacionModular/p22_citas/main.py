from citas import fecha, identificador

if __name__ == "__main__":
    print("=== SISTEMA DE CITA PREVIA BANCARIA ===")
    dias = int(input("¿Para dentro de cuántos días desea la cita?: "))
    print("----------------------------------")
    fecha_futura = fecha.obtener_fecha_cita_futura(dias)
    codigo_cita = identificador.generar_codigo_cita()
    print(f"Cita confirmada para el {fecha_futura}")
    print(f"Localizador de reserva: {codigo_cita}")
