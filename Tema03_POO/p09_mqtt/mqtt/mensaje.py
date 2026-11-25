class MensajeMQTT:
    def __init__(self, topic_in: str, valor_payload: float):
        self.topic = topic_in
        self.payload = valor_payload
