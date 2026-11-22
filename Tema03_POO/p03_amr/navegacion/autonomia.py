class CalculadorAutonomia:
    def estimar_distancia_m(
        self, pct_disponible: float, consumo_por_metro_val: float = 0.05
    ) -> float:
        return pct_disponible / consumo_por_metro_val
