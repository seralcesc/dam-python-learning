from verificador import estado, proceso

if __name__ == "__main__":
    archivo = input("Nombre del archivo de configuración: ")
    if proceso.es_fichero_valido(archivo):
        checksum = estado.simular_hash_archivo(archivo)
        print(f"Fichero correcto. Checksum: {checksum}")
    else:
        print("Error: El archivo no es válido.")
