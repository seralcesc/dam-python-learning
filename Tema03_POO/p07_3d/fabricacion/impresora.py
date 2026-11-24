class TrabajoImpresion3D:
    def __init__(
        self, id_pieza_in: str, num_capas: int, gramos_por_capa: float = 0.15
    ):
        self.id_pieza = id_pieza_in
        self.capas_totales = num_capas
        self.gramos_por_capa = gramos_por_capa

    def calcular_material_g(self) -> float:
        return self.gramos_por_capa * self.capas_totales
