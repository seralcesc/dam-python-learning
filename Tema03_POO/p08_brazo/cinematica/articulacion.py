class ServoArticulacion:
    def __init__(self, id_eje_in: str, angulo_in: float):
        self.id_eje = id_eje_in
        self._angulo_grados = angulo_in

    @property
    def angulo_grados(self) -> float:
        return self._angulo_grados

    def obtener_zona_trabajo(self) -> str:
        if self._angulo_grados > 170.0 or self._angulo_grados < 10.0:
            return "RIESGO_COLISIÓN"
        return "ZONA_SEGURA"
