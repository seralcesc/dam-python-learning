import datetime


def obtener_hora_solicitud():
    return datetime.datetime.now().strftime("%H:%M:%S")