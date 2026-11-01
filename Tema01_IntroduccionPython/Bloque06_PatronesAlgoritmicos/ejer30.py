# Ejercicio 30: Detector de Números Perfectos 
# Un número perfecto es aquel que es igual a la suma de sus divisores propios (excluyendo al 
# propio número). Crea un programa que determine si un número ingresado por el usuario es 
# perfecto (por ejemplo, el 6 es perfecto porque 1+2+3=6). 

numero = int(input("Introduce un número: "))
divisores = [i for i in range(1, numero) if numero % i == 0]
suma_divisores = sum(divisores)

if suma_divisores == numero:
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")