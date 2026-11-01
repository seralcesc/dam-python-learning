# Ejercicio 7: Formateador de Nombres de Usuarios
# Escribe un programa que pida el nombre completo de una persona. La salida debe mostrar:
# 1. El nombre completo en mayúsculas.
# 2. El nombre completo en minúsculas.
# 3. El nombre con la primera letra de cada palabra en mayúscula (Title Case).
# 4. La cantidad total de caracteres (sin contar los espacios en blanco).

nombre_completo = input("Introduce tu nombre completo: ")
nombre_mayusculas = nombre_completo.upper()
nombre_minusculas = nombre_completo.lower()
nombre_title = nombre_completo.title()
cantidad_caracteres = len(nombre_completo.strip())

print(f"1. El nombre completo en mayúsculas es: {nombre_mayusculas}")
print(f"2. El nombre completo en minúsculas es: {nombre_minusculas}")
print(f"3. El nombre con la primera letra de cada palabra en mayúscula es: {nombre_title}")
print(f"4. La cantidad total de caracteres (sin contar los espacios en blanco) es: {cantidad_caracteres}")