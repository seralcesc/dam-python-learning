# Ejercicio 13: Calculadora de Calificaciones Oficiales
# Escribe un programa que lea la nota numérica de un examen (entre 0 y 10, con decimales) y
# devuelva la calificación cualitativa según el criterio oficial:
# ● 0:5 Suspenso
# ● 5:6 Aprobado
# ● 6:7 Bien
# ● 7:9 Notable
# ● 9:10 Sobresaliente

# opcion a
nota = float(input("Introduce la nota del examen (0-10): "))
if nota < 0 or nota > 10:
    calificacion = "Nota no válida"
elif 0 <= nota < 5:
    calificacion = "Suspenso"
elif 5 <= nota < 6:
    calificacion = "Aprobado"
elif 6 <= nota < 7:
    calificacion = "Bien"
elif 7 <= nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

print(f"La calificación es: {calificacion}")

# opcion b
nota = float(input("Introduce la nota del examen (0-10): "))
if nota < 0 or nota > 10:
    calificacion = "Nota no válida"
elif nota < 5:
    calificacion = "Suspenso"
elif nota < 6:
    calificacion = "Aprobado"
elif nota < 7:
    calificacion = "Bien"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"
    
    print(f"La calificación es: {calificacion}")