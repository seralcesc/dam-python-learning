class GemeloHorno:
    def __init__(self, id_horno_in: str, temp_inicial_val: float):
        self.id_horno = id_horno_in
        self.__temperatura = temp_inicial_val

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    def enfriar(
        self, minutos_transcurridos: float, tasa_enfriamiento_val: float = 2.5
    ) -> float:
        perdida_calor = minutos_transcurridos * tasa_enfriamiento_val
        nueva_temp = self.__temperatura - perdida_calor
        if nueva_temp < -273.15:
            self.__temperatura = -273.15
        else:
            self.__temperatura = nueva_temp
        return self.__temperatura
