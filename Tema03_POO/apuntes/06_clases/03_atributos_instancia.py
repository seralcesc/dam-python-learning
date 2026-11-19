class Coche:
    # 1. ATRIBUTO DE CLASE (fuera del __init__)
    # Todos los objetos que creemos compartirán este mismo dato en memoria.
    ruedas = 4
    impuesto_circulacion = 50

    def __init__(self, marca, color):
        # 2. ATRIBUTOS DE INSTANCIA (dentro del __init__ con 'self.')
        # Cada objeto tiene su propia copia independiente.
        self.marca = marca
        self.color = color


# Creamos dos coches distintos
coche_1 = Coche("Seat", "Rojo")
coche_2 = Coche("Toyota", "Blanco")

# Ambos leen el atributo de clase sin problema
print(f"{coche_1.marca} tiene {coche_1.ruedas} ruedas.")  # 4 ruedas
print(f"{coche_2.marca} tiene {coche_2.ruedas} ruedas.")  # 4 ruedas

# --- ESCENARIO A: Cambiamos un atributo de INSTANCIA ---
coche_1.color = "Negro"
print(coche_1.color)  # Negro
print(coche_2.color)  # Blanco (No le afecta en absoluto)

# --- ESCENARIO B: Cambiamos el atributo de CLASE desde la Clase ---
# Sube el impuesto para TODOS los coches del país:
Coche.impuesto_circulacion = 80
print(coche_1.impuesto_circulacion)  # 80 (Se actualiza automáticamente)
print(coche_2.impuesto_circulacion)  # 80 (Se actualiza automáticamente)

##############################################################################
# ¡Cuidado con esta trampa típica de examen!
# Si se cambiar un atributo de clase usando un objeto concreto
# (por ejemplo: coche_1.ruedas = 3), no cambia las ruedas de todos los coches.
# Lo que hace Python es crearle a coche_1 un atributo de instancia nuevo
# llamado ruedas solo para él, mientras Coche.ruedas y coche_2.ruedas siguen
# valiendo 4. Para cambiarlo para todos, siempre se usa el nombre de la clase
# en mayúscula: Coche.ruedas = ....
##############################################################################
