# Ejercicio 25: Dibujo de Patrón de Asteriscos
# Pide la altura H de un triángulo y dibuja en consola un patrón como el siguiente 
# (para H-4)

H = int(input("Introduce la altura del triángulo (entero positivo): "))
if H <= 0:
    print("La altura debe ser un entero positivo.")
else:
    for i in range(1, H + 1):
        print('*' * i)