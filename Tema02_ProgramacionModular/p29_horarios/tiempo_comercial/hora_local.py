import datetime


def obtener_dia_semana_actual():
    return datetime.datetime.now().weekday()


def obtener_hora_24h_actual():
    return datetime.datetime.now().hour
