# Ejercicio 17: Sumador Continuo hasta Cero
# Escribe un programa que lea números enteros por teclado de manera continua y los vaya
# sumando. La lectura finalizará cuando el usuario introduzca el número 0. Al terminar, muestra la
# suma total.

suma_total = 0
while True:
    numero = int(input("Introduce un número entero (0 para finalizar): "))
    if numero == 0:
        break
    suma_total += numero

print(f"La suma total es: {suma_total}")