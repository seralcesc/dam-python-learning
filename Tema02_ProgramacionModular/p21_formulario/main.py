from validadores import numeros, texto

if __name__ == "__main__":
    print("=== FORMULARIO DE REGISTRO EN LÍNEA ===")
    nombre = input("Nombre de usuario: ")
    edad = int(input("Edad: "))

    nombre_valido = texto.es_texto_no_vacio(nombre)
    edad_valida = numeros.esta_en_rango(edad)
    registro_aceptado = nombre_valido and edad_valida

    print(f"[SISTEMA] Validando datos... ¿Registro aceptado?: {registro_aceptado}")
