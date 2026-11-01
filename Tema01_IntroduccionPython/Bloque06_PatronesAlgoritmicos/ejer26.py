# Ejercicio 26: Estadísticas de Evaluaciones 
# El usuario introducirá 5 notas de alumnos. Utiliza un contador y un acumulador para determinar 
# cuántos alumnos han aprobado y cuál es la nota media del grupo. 

num_alumnos = 5
contador_aprobados = 0
suma_notas = 0
while num_alumnos > 0:
    nota = float(input("Introduce la nota del alumno (0-10): "))
    if 0 <= nota <= 10:
        suma_notas += nota
        if nota >= 5:
            contador_aprobados += 1
        num_alumnos -= 1
    else:
        print("Nota inválida. Introduce un valor entre 0 y 10.")

if contador_aprobados > 0:
    nota_media = suma_notas / contador_aprobados
    print(f"Alumnos aprobados: {contador_aprobados}")
    print(f"Nota media: {nota_media:.2f}")
else:
    print("No hay alumnos aprobados.")