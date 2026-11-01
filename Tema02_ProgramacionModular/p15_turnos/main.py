from dispensador import generador, reloj_turno

print("=== DISPENSADOR AUTOMÁTICO DE TURNOS ===")

if __name__ == "__main__":
    turno = 0
  
    while True:
        input("Presiona [ENTER] para emitir ticket:")
        turno = generador.obtener_siguiente_turno(turno)
        hora = reloj_turno.obtener_hora_solicitud()
        print(f"Ticket #{turno} a las {hora}")

