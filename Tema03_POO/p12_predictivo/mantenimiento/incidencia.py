from datetime import datetime


class IncidenciaTecnica:
    __contador_id: int = 0

    def __init__(self, nom_maquina: str):
        self.maquina = nom_maquina
        IncidenciaTecnica.__contador_id += 1
        self.id_incidencia = IncidenciaTecnica.__contador_id

    def obtener_traza_mantenimiento(self) -> str:
        fecha = datetime.now().strftime("%Y-%m-%d")
        return (
            f"🛠️ [INCIDENCIA #{self.id_incidencia}] {fecha} "
            f"| Máquina: {self.maquina}"
        )
