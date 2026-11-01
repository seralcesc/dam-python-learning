# Ejercicio 3: Cálculo del Salario Bruto
# Diseña un script que pida las horas trabajadas en la semana por un desarrollador y su tarifa por
# hora en euros (decimal). El programa debe calcular y mostrar el salario bruto semanal.

horas_trabajadas = float(input("Introduce las horas trabajadas en la semana: "))
tarifa_por_hora = float(input("Introduce la tarifa por hora en euros: "))
salario_bruto = horas_trabajadas * tarifa_por_hora
print(f"El salario bruto semanal es: {salario_bruto} euros")
