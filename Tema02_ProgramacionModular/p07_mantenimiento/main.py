import datetime
from agenda.calendario import obtener_vista_mes
from agenda.citas import calcular_proxima_revision

if __name__ == "__main__":
    print("=== AGENDA TÉCNICA DE MANTENIMIENTO ===")

    dias_margen = int(input("¿En cuántos días corresponde la próxima revisión?: "))

    fecha_revision = calcular_proxima_revision(dias_margen)
    print(f"[SISTEMA] Próxima revisión técnica fijada para: {fecha_revision}\n")

    fecha_objetivo = datetime.datetime.strptime(fecha_revision, "%Y-%m-%d")

    calendario_mes = obtener_vista_mes(fecha_objetivo.year, fecha_objetivo.month)
    print(calendario_mes)