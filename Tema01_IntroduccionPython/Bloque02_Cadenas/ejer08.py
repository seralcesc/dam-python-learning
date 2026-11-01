# Ejercicio 8: Generador de Handles de Correo
# Crea un script que solicite el nombre y el primer apellido de un usuario y genere un correo
# corporativo del tipo nombre.apellido@iescastillodeluna.es en minúsculas y sin espacios.

nombre = input("Introduce tu nombre: ").strip().lower()
apellido = input("Introduce tu primer apellido: ").strip().lower()
correo = f"{nombre}.{apellido}@iescastillodeluna.es"
print(f"Tu correo corporativo es: {correo}")
