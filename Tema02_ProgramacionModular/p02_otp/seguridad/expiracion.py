import datetime

def obtener_hora_expiracion(minutos=5):
  hora_actual=datetime.datetime.now()
  expiracion=hora_actual+datetime.timedelta(minutes=minutos)
  return expiracion.strftime("%H:%M:%S")
