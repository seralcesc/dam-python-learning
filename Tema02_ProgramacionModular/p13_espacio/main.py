from disco import explorador, limpieza

if __name__ == "__main__":
    print("=== ORGANIZADOR Y LIMPIEZA DE DISCO ===")
    archivo=input("Introduce el nombre del archivo a comprobar: ")
    
    ruta_completa=explorador.construir_ruta(explorador.obtener_directorio_actual(), archivo)
    print(f"Ruta completa: {ruta_completa}")
    print(f"¿Es archivo temporal borrable?: {limpieza.es_archivo_temporal(archivo)}")