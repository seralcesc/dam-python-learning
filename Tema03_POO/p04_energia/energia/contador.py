class MedidorElectrico:
    def __init__(
        self, linea_nom: str, kwh_inicial: float, tarifa_kwh: float = 0.18
    ):
        self.linea_produccion = linea_nom
        self._kwh_consumidos = kwh_inicial
        self._precio_kwh = tarifa_kwh

    @property
    def kwh_consumidos(self) -> float:
        return self._kwh_consumidos

    @kwh_consumidos.setter
    def kwh_consumidos(self, nuevos_kwh: float) -> None:
        if nuevos_kwh < 0.0:
            nuevos_kwh = self._kwh_consumidos
        self._kwh_consumidos = nuevos_kwh

    def calcular_coste_total(self) -> float:
        coste_total = self._kwh_consumidos * self._precio_kwh
        return coste_total
