##############################################################################
# GETTERS
##############################################################################

# @property: Permite leer el dato como si fuera una variable normal
# print(cuenta.saldo), pero por debajo ejecuta una función.

##############################################################################
# SETTERS
##############################################################################

# @saldo.setter: Permite modificar el dato (cuenta.saldo = 500), pero pasando antes por un filtro de seguridad (un if) para validar que el dato tiene sentido.


########################### IMPORTANTE: ###########################
# Dentro de @property y @setter es el único sitio donde debes usar los guiones bajos


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial  # Protegido con un guion bajo

    @property
    def saldo(self):  # GETTER: Para leer el saldo
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):  # SETTER: Para modificarlo con seguridad
        if nuevo_saldo < 0:
            print("Error: No puedes dejar la cuenta en números rojos.")
        else:
            self._saldo = nuevo_saldo


mi_cuenta = CuentaBancaria("Sergio", 1000)
print(mi_cuenta.saldo)  # Llama al @property -> Imprime 1000
mi_cuenta.saldo = (
    -50
)  # Llama al @saldo.setter -> Salta el error y no lo cambia


class Producto:
    def __init__(self, nombre, precio_inicial):
        self.nombre = nombre
        # OJO: Fíjate que aquí NO pongo 'self._precio = precio_inicial'.
        # Pongo 'self.precio = precio_inicial' para obligar a que, incluso al nacer, el dato pase por el filtro del @precio.setter.
        self.precio = precio_inicial

    # 1. GETTER (Lectura): Se activa cuando haces print(p.precio)
    @property
    def precio(self):
        return (
            self._precio
        )  # Devuelve el valor real que está guardado con guion bajo

    # 2. SETTER (Escritura con validación): Se activa cuando haces p.precio = algo
    @precio.setter
    def precio(self, nuevo_valor):
        if nuevo_valor <= 0:
            print(
                f"❌ Error: El precio '{nuevo_valor}€' no es válido. Se asigna 1€ por defecto."
            )
            self._precio = 1.0
        else:
            print(f"✅ Precio actualizado correctamente a {nuevo_valor}€")
            self._precio = nuevo_valor


# --- PRUEBA ---

# 1. Creamos un producto con precio correcto
teclado = Producto("Teclado Mecánico", 65.50)
# Salida: ✅ Precio actualizado correctamente a 65.5€

# 2. Leemos el precio (Parece que leemos una variable, pero se ejecuta el @property)
print(f"El {teclado.nombre} cuesta {teclado.precio}€")
# Salida: El Teclado Mecánico cuesta 65.5€

# 3. Intentamos hacer trampa poniendo un precio negativo (Se ejecuta el @precio.setter)
teclado.precio = -20
# Salida: ❌ Error: El precio '-20€' no es válido. Se asigna 1€ por defecto.

# 4. Comprobamos qué precio se ha quedado guardado realmente
print(f"Precio final tras el intento: {teclado.precio}€")
# Salida: Precio final tras el intento: 1.0€
