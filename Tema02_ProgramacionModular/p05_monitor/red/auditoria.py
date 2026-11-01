import time
import random

def medir_latencia_simulada():
    inicio = time.time()
    time.sleep(random.uniform(0.05, 0.2))
    fin = time.time()
    latencia = (fin - inicio) * 1000  # Convertir a milisegundos
    return round(latencia, 1)