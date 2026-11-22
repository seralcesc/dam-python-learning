class SensorVibracion:
    def __init__(self, id_motor_in: str, vibracion_rms_val: float):
        self.id_motor = id_motor_in
        self.vibracion_rms = vibracion_rms_val

    @property
    def vibracion_rms(self) -> float:
        return self._vibracion_rms

    @vibracion_rms.setter
    def vibracion_rms(self, nuevo_valor: float) -> None:
        if nuevo_valor < 0.0:
            raise ValueError("La vibración RMS no puede ser negativa")
        self._vibracion_rms = nuevo_valor
