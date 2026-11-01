# Ejercicio 28: Filtro y Acumulador de Ventas 
# Simula un sistema de ventas. Procesa una lista predefnida de importes de ventas [45, 120, 230, 
# 80, 500, 15]. Cuenta cuántas ventas superan los 100€, acumula el total de dichas ventas 
# "destacadas" e indica mediante un fag si se ha superado un objetivo global de 700€. 

ventas = [45, 120, 230, 80, 500, 15]
ventas_destacadas = [venta for venta in ventas if venta > 100]
total_ventas_destacadas = sum(ventas_destacadas)
objetivo = 700
se_ha_superado_objetivo = total_ventas_destacadas > objetivo

if se_ha_superado_objetivo:
    print("Se ha superado el objetivo global.")
else:
    print("No se ha superado el objetivo global.")