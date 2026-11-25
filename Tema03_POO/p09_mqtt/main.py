# ============================================================
# Autor:       Sergio Alcántara
# Fecha:       25/11/2026
# Archivo:     main.py
# Ejercicio:   Proyecto 9: Parser Protocolo MQTT Industrial
# Descripción: 2 Paquetes: mqtt / parsers
#
# Extraer el topic y la carga útil (payload) de una trama de telemetría
# MQTT industrial utilizando expresiones regulares (re).
# =======================================================

import sys

from mqtt.mensaje import MensajeMQTT
from parsers.mqtt_parser import ParserMQTT


def ejecutar_aplicacion():
    print("=== PARSER DE PROTOCOLOS IIOT MQTT ===")
    if len(sys.argv) == 2:
        cadena_trama = sys.argv[1]
    else:
        cadena_trama = input("Introduce la trama recibida (TOPIC=PAYLOAD): ")

    print("-------------------------------------------")

    parser = ParserMQTT()
    topic, payload = parser.parsear_trama(cadena_trama)
    mensaje = MensajeMQTT(topic, payload)
    print(
        f"📡 [MQTT PARSED] Topic: {mensaje.topic} | Payload: {mensaje.payload}"
    )


if __name__ == "__main__":
    ejecutar_aplicacion()
