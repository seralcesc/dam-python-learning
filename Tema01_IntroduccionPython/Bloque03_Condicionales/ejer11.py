# Ejercicio 11: Clasificador de Números
# Pide un número entero al usuario e indica mediante un condicional si el número es positivo,
# negativo o cero, y si además es par o impar.

numero = int(input("Introduce un número entero: "))
if numero > 0:
    tipo = "positivo"
elif numero < 0:
    tipo = "negativo"
else:
    tipo = "cero"

if numero % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"

print(f"El número {numero} es {tipo} y {paridad}.")