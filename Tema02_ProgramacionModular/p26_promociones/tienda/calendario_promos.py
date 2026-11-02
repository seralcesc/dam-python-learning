import datetime


def es_mes_promocional(mes_target=11):
    mes_actual = datetime.datetime.now().month
    return mes_actual == mes_target
