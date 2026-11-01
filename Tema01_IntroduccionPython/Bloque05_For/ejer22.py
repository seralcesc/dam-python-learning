# Ejercicio 22: Generador de Pares en Rango
# Pide dos números enteros: un límite inferior y un límite superior. Imprime todos los números
# pares comprendidos en ese intervalo (inclusive).

minimo = int(input("Introduce el límite inferior: "))
maximo = int(input("Introduce el límite superior: "))
for i in range(minimo, maximo + 1):
    if i % 2 == 0:
        print(i)
