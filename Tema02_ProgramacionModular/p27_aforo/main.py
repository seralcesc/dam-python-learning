from control_acceso import contador, limite

if __name__ == "__main__":
    print("=== CONTROL DE AFORO EN TORNO ===")
    actual = int(input("Aforo actual dentro del local: "))
    cola = int(input("Personas en la puerta intentando entrar: "))

    print("---------------------------------")
    total = contador.sumar_asistentes(actual, cola)
    maximo = 100
    if limite.supera_aforo_maximo(total, maximo):
        print(f"BLOQUEADO: Se supera la capacidad máxima autorizada ({maximo} pers).")
    else:
        print(
            f"PERMITIDO: No se supera la capacidad máxima ({maximo} pers). Aforo total: {total} pers."
        )
