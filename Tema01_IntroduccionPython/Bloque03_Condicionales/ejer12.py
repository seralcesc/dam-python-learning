# Ejercicio 12: Control de Acceso al Servidor
# Para acceder a un servidor del centro se requiere tener al menos 18 años y poseer el rol de
# "admin" o "profesor". Escribe un script que pida la edad y el rol del usuario y determine si tiene
# acceso concedido.

edad = int(input("Introduce tu edad: "))
rol = input("Introduce tu rol (admin/profesor/estudiante): ").strip().lower()

if edad >= 18 and rol in ["admin", "profesor"]:
    print("Acceso concedido al servidor.")
else:
    print("Acceso denegado al servidor.")