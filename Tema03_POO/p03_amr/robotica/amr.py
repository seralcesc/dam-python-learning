class RobotAMR:
    def __init__(self, id_robot_in: str, bateria_pct_val: float):
        self.id_robot = id_robot_in
        self.__bateria_pct = bateria_pct_val

    @property
    def bateria_pct(self) -> float:
        return self.__bateria_pct
