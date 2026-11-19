class Jugador:
    def __init__(self, alias, puntuacion, password):
        self.alias = alias  # PÚBLICO: Acceso libre
        self._puntuacion = (
            puntuacion  # PROTEGIDO: Aviso de "no tocar directamente"
        )
        self.__password = password  # PRIVADO: Python le cambia el nombre (Name mangling) para esconderlo y que de error si alguien lo llama desde fuera


j1 = Jugador("Seralcesc", 1500, "1234")

# 1. Público -> Funciona normal
print(j1.alias)  # Imprime: Seralcesc

# 2. Protegido -> Python te deja verlo, pero por ética profesional y buenas prácticas no debería hacerse así
print(j1._puntuacion)  # Imprime: 1500

# 3. Privado -> Si se descomenta la línea de abajo, el programa EXPLOTA (AttributeError)
# print(j1.__password)

# ¿Por qué? Porque Python le hizo "Name Mangling" (le cambió el nombre):
# print(j1._Jugador__password)  # Imprime: 1234 (Así lo guarda Python por detrás)
