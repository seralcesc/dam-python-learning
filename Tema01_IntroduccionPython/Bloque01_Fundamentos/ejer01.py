
# Ejercicio 1: Registro de Alumno
# Escribe un programa que solicite por consola el nombre del alumno, sus apellidos y su ciclo
# formativo. Posteriormente, debe mostrar un mensaje de bienvenida unificado utilizando
# cadenas formateadas (f-strings).

nombre=input("Introduce el nombre del alumno: ")
apellidos=input("Introduce los apellidos del alumno: ")
ciclo=input("Introduce el ciclo formativo: ")

print(f"¡Bienvenido, {nombre} {apellidos}! Estás inscrito en el ciclo {ciclo}.")