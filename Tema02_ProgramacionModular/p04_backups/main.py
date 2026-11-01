import sys

from almacenamiento import archivos, compresion

if __name__ == "__main__":
    if archivos.existe_archivo("main.py"):
        print("[SISTEMA] Verificando integridad del proyecto... OK")
    else:
        print("[SISTEMA] Verificando integridad del proyecto... ERROR: 'main.py' no encontrado.")
        sys.exit(1)

    nombre_copia = input("Introduce el nombre para el archivo de respaldo: ")


    print(f"[SISTEMA] Creando archivo '{nombre_copia}.zip'...")
    if compresion.crear_copia_zip(f"{nombre_copia}.zip", "almacenamiento"):
        print("Proceso finalizado con éxito.")
    else:
        print("Error al crear la copia de seguridad.")