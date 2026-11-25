from fabricacion.impresora import TrabajoImpresion3D


class EstimadorImpresion:
    def calcular_tiempo_min(
        self, trabajo_obj: TrabajoImpresion3D, seg_por_cap_val: float = 12.0
    ) -> float:
        tiempo_en_minutos = (trabajo_obj.capas_totales * seg_por_cap_val) / 60
        return tiempo_en_minutos
