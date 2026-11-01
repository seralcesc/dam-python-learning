from reportes import exportar, sumas

if __name__ == "__main__":
    print("=== GENERADOR DE INFORMES CONTABLES ===")
    anyo = int(input("Año fiscal: "))
    trimestre = int(input("Trimestre (1-4): "))
    total_acumulado = sumas.sumar_tres_meses(3200.34, 4500.50, 3900.75)
    print(
        f"Total acumulado: {total_acumulado}€ | Nombre archivo: {exportar.generar_nombre_reporte(anyo, trimestre)}"
    )
