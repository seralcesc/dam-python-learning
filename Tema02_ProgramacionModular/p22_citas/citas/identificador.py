import random


def generar_codigo_cita():
    codigo = random.randint(1000, 9999)
    return f"CITA-{codigo}"
