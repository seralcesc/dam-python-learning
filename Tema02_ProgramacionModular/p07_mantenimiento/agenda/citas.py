import datetime


def calcular_proxima_revision(dias_margen):
    fecha_hoy = datetime.date.today()
    fecha_proxima = fecha_hoy + datetime.timedelta(days=dias_margen)
    return fecha_proxima.strftime("%Y-%m-%d")
