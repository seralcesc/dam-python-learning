from fabricacion.impresora import TrabajoImpresion3D


class EstimadorImpresion:
    def calcular_tiempo_min(
        self, trabajo_obj: TrabajoImpresion3D, seg_por_cap_val: float = 12.0
    ) -> float:
        segundos_por_capa = seg_por_cap_val
        trabajo_obj = trabajo_obj.capas_totales
        tiempo_en_minutos = (trabajo_obj * segundos_por_capa) / 60
        return tiempo_en_minutos
