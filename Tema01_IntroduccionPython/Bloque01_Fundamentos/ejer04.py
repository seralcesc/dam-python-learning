# Escribe un programa que solicite una cantidad total de segundos (entero) y calcule a cuántas
# horas, minutos y segundos equivalen.
# Pista: Utiliza división entera (//) y el operador módulo (%).

total_segundos = int(input("Introduce la cantidad total de segundos: "))
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60
print(f"{total_segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos.")