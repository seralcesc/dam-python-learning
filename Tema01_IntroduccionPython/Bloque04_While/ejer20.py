# Ejercicio 20: Algoritmo de Collatz
# Pide un número entero positivo. Si es par, se divide entre 2. Si es impar, se multiplica por 3 y se
# le suma 1. Repite este proceso mostrando cada número hasta llegar a 1.

numero = int(input("Introduce un número entero positivo: "))
while numero != 1:
    print(numero)
    if numero % 2 == 0:
        numero //= 2
    else:
        numero = 3 * numero + 1
print(numero)