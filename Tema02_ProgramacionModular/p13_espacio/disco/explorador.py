import os

def obtener_directorio_actual():
    ruta=os.getcwd()
    return ruta
  
def construir_ruta(carpeta, archivo):
    ruta_unificada=os.path.join(carpeta, archivo)
    return ruta_unificada