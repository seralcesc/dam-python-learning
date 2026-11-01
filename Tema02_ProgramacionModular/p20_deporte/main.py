from crono import medicion, serie

if __name__ == "__main__":
    print("=== CRONÓMETRO DE ENTRENAMIENTO ===")
    segundos = float(input("Segundos de pausa de entrenamiento: "))

    inicio = medicion.obtener_marca_tiempo()
    print("[CRONO] Iniciando descanso...")

    serie.pausa_descanso(segundos)

    fin = medicion.obtener_marca_tiempo()
    pausa = medicion.diferencia_tiempo(inicio, fin)

    print(f"[CRONO] Tiempo de descanso completado: {pausa} segundos")
