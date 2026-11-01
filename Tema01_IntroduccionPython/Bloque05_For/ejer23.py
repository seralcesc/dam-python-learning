# Ejercicio 23: Contador de Vocales
# Dado un texto introducido por el usuario, utiliza un bucle for para contar cuántas vocales (a, e, i,
# o, u) contiene en total.

vocales = "aeiouAEIOU"
texto = input("Introduce un texto: ")
contador = 0
for caracter in texto:
    if caracter in vocales:
        contador += 1
print(f"El texto contiene {contador} vocales.")