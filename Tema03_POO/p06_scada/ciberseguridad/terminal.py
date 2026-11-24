class TerminalSCADA:
    def __init__(self, id_terminal_in: str, token_secreo: str):
        self.id_terminal = id_terminal_in
        self.__intentos_fallidos = 0
        self.__token_seguridad = token_secreo

    @property
    def intentos_fallidos(self) -> int:
        return self.__intentos_fallidos

    def validar_acceso(self, token_probado: str) -> bool:
        if token_probado == self.__token_seguridad:
            return True
        self.__intentos_fallidos += 1
        return False
