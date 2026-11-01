from conversion import distancia, velocidad

if __name__ == "__main__":
    print("--- CONVERSOR DE NAVEGACIÓN MARÍTIMA ---")
    nudos=float(input("Introduce la velocidad de la nave (nudos): "))
    millas=float(input("Introduce la distancia a puerto (millas): "))
    print("----------------------------------------")
    print("EQUIVALENCIA TÉCNICA:")
    kmh=velocidad.nudos_a_kmh(nudos)
    metros=distancia.millas_a_metros(millas)
    print(f"Velocidad: {kmh:.2f} km/h | Distancia: {metros} metros.")
