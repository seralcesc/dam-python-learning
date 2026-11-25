class MyEmptyPerson:
    pass  # Crea una clase, y el pass le da valor nulo para evitar errores.


# Se crea un fichero para cada clase, y alli se escribe todo lo relacionado con esa clase. Y se llama desde fuera, a la clase.


# Crea la clase, y la primera funcion es la de crear objetos con los parametros que le asignemos.


class Perro:  # El molde
    pass


# Instanciamos (creamos dos perros reales en memoria)
toby = Perro()
luna = Perro()
# toby y luna son dos objetos distintos, aunque vengan del mismo molde.


class Person:
    # constructor de clases. self es obligatorio
    def __init__(self, name, surname, alias="Sin alias"):
        self.name = name
        self.surname = surname
        self.alias = alias
        self.fullname = f"{name} {surname} ({alias})"

    # dentro de la clase podemos crear funciones. con el self como parametro, nos deja llamar a las propiedades de la propia clase.
    def walk(self):
        print(f"{self.fullname} está caminando")


# My_person y other_person son dos objetos creados a partir de la clase.
# Los parámertos introducidos son sus características.
my_person = Person("Sergio", "Alcántara")
print(f"{my_person.name} {my_person.surname}")
print(my_person.fullname)

other_person = Person("Bruno", "Alcántara", "Brunete")
