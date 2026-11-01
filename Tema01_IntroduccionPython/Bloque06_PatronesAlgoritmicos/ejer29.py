# Ejercicio 29: Registro del Mayor y Menor Número 
# Solicita al usuario la cantidad de números que desea introducir. A continuación, pide esa 
# cantidad de números enteros y determina cuál ha sido el valor máximo y cuál el mínimo 
# introducido. 

cantidad = int(input("¿Cuántos números deseas introducir? "))
numeros = []

for _ in range(cantidad): # _ se utiliza como variable de bucle cuando no se necesita su valor
    numero = int(input("Introduce un número: "))
    numeros.append(numero) 

maximo = max(numeros)
minimo = min(numeros)

print(f"El valor máximo introducido es: {maximo}")
print(f"El valor mínimo introducido es: {minimo}")