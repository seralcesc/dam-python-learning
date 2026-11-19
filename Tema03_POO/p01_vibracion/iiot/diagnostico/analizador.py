from iiot.vibracion import SensorVibracion


class AnalizadorVibracion:
    def evaluar_estado(self, sensor_obj: SensorVibracion) -> str:
        if sensor_obj._vibracion_rms > 7.1:
            return "CRÍTICO"
        else:
            return "NORMAL"
