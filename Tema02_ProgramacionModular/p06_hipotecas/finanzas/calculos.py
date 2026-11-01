import math


def calcular_cuota_mensual(capital, interes_anual, meses):
    interes_mensual = (interes_anual / 12) / 100
    # Fórmula de cuota mensual: C = (P * r) / (1 - (1 + r)^-n)
    # P = capital, r = interes_mensual, n = meses, C = cuota mensual
    cuota = (capital * interes_mensual) / (1 - math.pow(1 + interes_mensual, -meses))
    return cuota