import fichaje.reloj as reloj
import fichaje.validar as validar

if __name__ == "__main__":
    print("=== TERMINAL AUTO-FICHAJE DE EMPLEADOS ===")
    print("[SISTEMA] Registrando fichaje de entrada...")
    
    hora_fichaje = reloj.obtener_hora_actual()
    print(f"Hora oficial capturada: {hora_fichaje}")
    
    if validar.es_horario_laboral(hora_fichaje, "09:00"):
        print("Estado de entrada: PUNTUAL (Llegada antes de las 09:00)")
    else:
        print("Estado de entrada: RETRASO (Llegada después de las 09:00)")
    
    print("-------------------------------------------")
    hora_salida = input("Introduce tu hora prevista de salida (HH:MM): ")
    
    minutos_trabajados = reloj.calcular_minutos_transcurridos(hora_fichaje, hora_salida)
    print(f"Duración total de tu jornada de hoy: {int(minutos_trabajados)} minutos.")