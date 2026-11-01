# Ejercicio 15: Comprobador de Años Bisiestos
# Un año es bisiesto si es divisible por 4, pero no por 100, salvo que también sea divisible por
# 400. Crea un programa que determine si un año introducido por teclado cumple estas
# condiciones.

año = int(input("Introduce un año: "))
if año % 400 == 0:
    es_bisiesto = True
elif año % 100 == 0:
    es_bisiesto = False
elif año % 4 == 0:
    es_bisiesto = True
else:
    es_bisiesto = False

if es_bisiesto:
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")