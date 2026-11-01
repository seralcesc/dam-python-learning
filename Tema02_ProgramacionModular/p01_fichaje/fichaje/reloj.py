import datetime

def obtener_hora_actual():
    ahora = datetime.datetime.now()
    return ahora.strftime("%H:%M")
  
def calcular_minutos_transcurridos(hora_inicio_str, hora_fin_str):
    formato_hora = "%H:%M"
    inicio = datetime.datetime.strptime(hora_inicio_str, formato_hora)
    fin = datetime.datetime.strptime(hora_fin_str, formato_hora)
    diferencia = fin - inicio
    return diferencia.total_seconds() / 60