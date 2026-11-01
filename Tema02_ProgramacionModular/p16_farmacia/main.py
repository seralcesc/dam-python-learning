from medicina import dosis, paciente

if __name__ == "__main__":
    print("=== ASISTENTE DE DOSIFICACIÓN FARMACEÚTICA ===")
    edad = int(input("Edad del paciente: "))
    f1_n, f1_d = 1, 4
    f2_n, f2_d = 1, 2
    print(f"Numerador toma 1: {f1_n} | Denominador toma 1: {f1_d}")
    print(f"Numerador toma 2: {f2_n} | Denominador toma 2: {f2_d}")
    print(
        f"Dosis total acumulada: {dosis.sumar_fraccion_dosis(f1_n, f1_d, f2_n, f2_d)} de ampolla | Paciente pediátrico: {paciente.es_dosis_pediatrica(edad)}"
    )
