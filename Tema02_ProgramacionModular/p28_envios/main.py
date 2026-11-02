from logistica import peso, precio

if __name__ == "__main__":
    print("=== TARIFICADOR DE ENVÍOS EXPRESS ===")
    peso_kg = float(input("Peso del paquete en báscula: "))
    print("[SISTEMA] Redondeando tramo al kilo superior...")
    peso_redondeado = peso.redondear_peso_superior(peso_kg)
    coste = precio.calcular_tarifa_envio(peso_redondeado)
    print(
        f"Peso facturable: {peso_redondeado} kg | Coste total del envío: {coste:.2f} €"
    )
