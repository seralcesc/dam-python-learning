from automatizacion.plc import ControladorPLC


class ValidadorRedOT:
    def es_ip_valida(self, direccion_ip: str) -> bool:
        ip_base = "192.168.10."
        return direccion_ip[0:11] == ip_base
