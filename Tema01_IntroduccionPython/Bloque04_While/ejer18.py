# Ejercicio 18: Contador Regresivo
# Pide un número entero positivo e imprime una cuenta atrás desde ese número hasta 0 usando
# un bucle while.

numero = int(input("Introduce un número entero positivo: "))
while numero >= 0:
    print(numero)
    numero -= 1