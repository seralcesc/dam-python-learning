# Ejercicio 16: Validación de Contraseña
# Crea un programa que solicite una clave de acceso. El programa debe repetir la petición
# mientras la clave introducida sea incorrecta. Permite un máximo de 3 intentos antes de
# bloquear el acceso.

i=3
while i > 0:
    clave = input("Introduce la clave de acceso: ")
    if clave == "1234":
        print("Acceso concedido.")
        break
    else:
        i -= 1
        print(f"Clave incorrecta. Te quedan {i} intentos.")

if i == 0:
    print("Acceso bloqueado.")
