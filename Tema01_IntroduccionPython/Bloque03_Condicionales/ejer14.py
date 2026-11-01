# Ejercicio 14: Tarifario con Descuento
# Un parque temático cobra 12€ por entrada. Sin embargo:
# ● Los menores de 4 años entran gratis.
# ● Los estudiantes o mayores de 65 años tienen un 40% de descuento.
# ● El resto paga la tarifa completa.
# Solicita edad y si es estudiante (s/n) para calcular el precio final a pagar.

edad = int(input("Introduce tu edad: "))
es_estudiante = input("¿Eres estudiante? (s/n): ").strip().lower() == 's'
entrada_base = 12.0

if edad < 4:
    precio_final = 0.0
elif es_estudiante or edad >= 65:
    precio_final = entrada_base * 0.6
else:
    precio_final = entrada_base

print(f"El precio final a pagar es: {precio_final:.2f}€")