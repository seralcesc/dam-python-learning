from finanzas import calculos, formato

if __name__ == "__main__":
    print("--- SIMULADOR DE PRÉSTAMOS BANCARIOS ---")
    capital_solicitado = float(input("Introduce el capital solicitado (€): "))
    interes = float(input("Introduce el porcentaje de interés anual (%): "))
    plazo_meses = int(input("Introduce los meses de amortización (ej. 300): "))
    print("-------------------------------------------")
    
    cuota = calculos.calcular_cuota_mensual(capital_solicitado, interes, plazo_meses)
    
    print("RESUMEN CONCESIÓN PRÉSTAMO")
    formato.mostrar_resumen_prestamo(capital_solicitado, cuota)