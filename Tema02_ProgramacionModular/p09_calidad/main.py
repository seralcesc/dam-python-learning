from control import estadisticas, tolerancias

if __name__ == "__main__":
    print("=== CONTROL DE CALIDAD ===")
    m1=float(input("Ingrese medida de muestra 1 (mm): "))
    m2=float(input("Ingrese medida de muestra 2 (mm): "))
    m3=float(input("Ingrese medida de muestra 3 (mm): "))
    print("--------------------------------")
    promedio = estadisticas.calcular_media_piezas(m1, m2, m3)
    
    if tolerancias.esta_en_tolerancia(promedio):
        print(f"Medida del lote: {promedio} mm -> ESTADO: LOTE ACEPTADO")
    else:
        print(f"Medida del lote: {promedio} mm -> ESTADO: LOTE RECHAZADO")