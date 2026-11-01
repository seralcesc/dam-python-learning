import math

def esta_en_tolerancia(medida, nominal=10.0, margen=0.5):
    desviacion_absoluta=math.fabs(medida-nominal)
    return desviacion_absoluta<=margen
