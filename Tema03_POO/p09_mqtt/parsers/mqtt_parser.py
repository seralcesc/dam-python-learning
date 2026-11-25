import re


class ParserMQTT:
    def parsear_trama(self, cadena_trama: str) -> tuple[str, float]:
        coincidencia = re.match(r"^([^=]+)=(.+)$", cadena_trama.strip())
        if not coincidencia:
            raise ValueError(f"Trama MQTT inválida: {cadena_trama}")
        topic = coincidencia.group(1)
        payload = float(coincidencia.group(2))
        return (topic, payload)
