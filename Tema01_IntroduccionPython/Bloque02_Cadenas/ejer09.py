# Ejercicio 9: Detector de Subcadenas
# Pide al usuario un texto largo y una palabra de búsqueda. El programa debe indicar mediante
# un booleano (True/False) si la palabra está presente en el texto, ignorando diferencias entre
# mayúsculas y minúsculas.

texto = input("Introduce un texto largo: ").lower()
palabra_busqueda = input("Introduce la palabra de búsqueda: ").lower()
esta_presente = palabra_busqueda in texto
print(f"La palabra '{palabra_busqueda}' está presente en el texto: {esta_presente}")