# Ejercicio 21: Tabla de Multiplicar
# Solicita un número entero del 1 al 10 e imprime su tabla de multiplicar completa (del 1 al 10) con
# el formato X x Y = Z.

numero = int(input("Introduce un número entero del 1 al 10: "))
if 1 <= numero <= 10:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")