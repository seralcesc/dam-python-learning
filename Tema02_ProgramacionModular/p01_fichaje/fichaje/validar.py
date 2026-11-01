import datetime

# es_horario_laboral(hora_entrada_str, hora_limite_str="09:00"): Recibe la hora de entrada 
# hora_entrada_str (str) y opcionalmente la hora límite hora_limite_str (str, por defecto `"09:00"`). 
# Compara si la hora de entrada es menor o igual al límite y devuelve un booleano bool (True si es 
# puntual).

def es_horario_laboral(hora_entrada_str, hora_limite_str="09:00"):
    return hora_entrada_str <= hora_limite_str