class ConversorVariador:
    @staticmethod
    def hz_a_rpm(frecuencia_hz: float, num_pares_polos: int = 2) -> float:
        return (60 * frecuencia_hz) / num_pares_polos
