class Perro:
    # este es el constructor. Siempre lleva __init__, y el primer parametro de la función siempre es el self, que es lo que asocia cada argumento de la función con las propiedades de cada objeto.
    def __init__(self, nombre_dado, raza_dada):
        self.nombre = nombre_dado  # Guarda el dato EN ESTE perro
        self.raza = raza_dada

    # esto es un método de la clase, y aquí el self nos permite acceder a los atrobutos de la clase. Se utiliza al crear el método, no al llamarlo.
    def presentarse(self):
        # Usa 'self.nombre' para leer SU propio nombre, no el de otro perro
        print(f"Guau, soy {self.nombre} y soy un {self.raza}")


toby = Perro(
    "Toby", "Beagle"
)  # Python pasa 'toby' como 'self' automáticamente
luna = Perro("Luna", "Pastor Alemán")

toby.presentarse()  # Imprime: Guau, soy Toby y soy un Beagle
