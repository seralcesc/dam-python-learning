import time


def obtener_marca_tiempo():
    return time.time()


def diferencia_tiempo(inicio, fin):
    diferencia = fin - inicio
    return round(diferencia, 1)
