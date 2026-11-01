# Ejercicio 2: Conversor de Temperatura
# Crea un programa que pida una temperatura en grados Celsius (permitiendo valores
# decimales) y la transforme a grados Fahrenheit.

celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")