class ControladorPLC:
    def __init__(self, id_plc_in: str, ip_cfg: str):
        self.id_plc = id_plc_in
        self.ip_control = ip_cfg
