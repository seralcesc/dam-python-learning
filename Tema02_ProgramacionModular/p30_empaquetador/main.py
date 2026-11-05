from empaquetado import comprobacion, zip_engine

if __name__ == "__main__":
    print("=== EMPAQUETADOR DE PROYECTOS EN ARCHIVO ZIP ===")
    ruta = input("Ruta o nombre de la carpeta a comprimir: ")

    if comprobacion.es_directorio_valido(ruta):
        nombre_salida = input(
            "Nombre del archivo ZIP de salida (sin extensión): "
        )
        print("[SISTEMA] Comprimiendo archivos...")
        archivo_generado = zip_engine.comprimir_proyecto(nombre_salida, ruta)
        print(
            f"¡Éxito! Proyecto empaquetado correctamente en: {nombre_salida}.zip"
        )
    else:
        print(
            "[ERROR] La ruta especificada no existe o no es un directorio válido."
        )
