import datetime


def obtener_fecha_cita_futura(dias):
    hoy = datetime.datetime.today()
    fecha_futura = hoy + datetime.timedelta(days=dias)
    return fecha_futura.strftime("%d/%m/%Y")
