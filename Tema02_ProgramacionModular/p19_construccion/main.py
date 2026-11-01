from geometria import superficies, triangulos

if __name__ == "__main__":
    print("=== CALCULADORA TÉCNICA DE OBRAS ===")
    ancho = float(input("Ancho de la habitación (m): "))
    largo = float(input("Largo de la habitación (m): "))
    print("-------------------------------------------")
    area = superficies.area_rectangulo(ancho, largo)
    diagonal = triangulos.calcular_hipotenusa(ancho, largo)
    print(
        f"Superficie a embaldosar: {area:.1f} m² | Diagonal estructural: {diagonal:.2f} m"
    )
