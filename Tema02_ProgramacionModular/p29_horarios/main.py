from tiempo_comercial import apertura, hora_local

if __name__ == "__main__":
    print("=== COMUNICADOR DE HORARIO ATENCIÓN AL CLIENTE ===")
    print("[SISTEMA] Consultando reloj del servidor...")

    dia = hora_local.obtener_dia_semana_actual()
    hora = hora_local.obtener_hora_24h_actual()

    dia_comercial = apertura.es_dia_laborable(dia)
    horario = 9 <= hora < 20

    if dia_comercial and horario:
        estado = "ABIERTO (Horario comercial activo)."
    else:
        estado = "CERRADO (Horario comercial inactivo)"

    print(f"Estado actual de la oficina: {estado} ")
