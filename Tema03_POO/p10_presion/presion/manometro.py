import statistics


class ManometroDigital:
    def __init__(self, nom_circuito: str):
        self.circuito = nom_circuito
        self.__presiones_bar: list[float] = []

    @property
    def presiones_bar(self):
        return self.__presiones_bar

    def agregar_presion(self, valor_bar: float) -> None:
        self.__presiones_bar.append(valor_bar)

    def calcular_media_bar(self) -> float:
        if not self.__presiones_bar:
            return 0.0
        return statistics.mean(self.__presiones_bar)
