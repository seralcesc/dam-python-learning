import datetime

def obtener_hora_actual():
  hora_actual = datetime.datetime.now().strftime("%d/%m/%Y a las %H:%M")
  return hora_actual

def formatear_moneda(importe):
  return f"{importe:.2f} €"