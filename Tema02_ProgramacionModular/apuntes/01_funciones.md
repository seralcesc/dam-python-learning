# 01 · Funciones: entradas, proceso y resultado

[Índice del tema](../README.md) · [Siguiente: módulos y paquetes](02_modulos_paquetes.md)

**Aplicación:** todos los proyectos. Empieza aquí aunque ya hayas escrito funciones.

## 1. Para qué sirve una función

Una función agrupa instrucciones bajo un nombre para realizar una tarea. Permite reutilizar una operación y comprobarla por separado.

```python
def calcular_importe(unidades, precio_unitario):
    importe = unidades * precio_unitario
    return importe

total = calcular_importe(3, 2.5)
print(total)  # 7.5
```

| Parte | Significado |
|---|---|
| def | Comienza la definición |
| calcular_importe | Nombre de la función |
| unidades, precio_unitario | Parámetros: nombres que reciben datos |
| : y sangría | Delimitan el cuerpo |
| return importe | Devuelve el resultado a quien llama |
| calcular_importe(3, 2.5) | Llamada con dos argumentos |
| total = ... | Guarda el valor devuelto |

Definir una función no ejecuta su cuerpo. La llamada sí lo hace.

## 2. Parámetro y argumento

Un **parámetro** aparece en la definición. Un **argumento** es el valor que pasas en una llamada.

En el ejemplo anterior, unidades es un parámetro y 3 es el argumento que recibe. En otra llamada puede recibir 12 sin cambiar la función.

```python
def calcular_importe(unidades, precio_unitario):
    return unidades * precio_unitario

cantidad = 4
precio = 6
resultado = calcular_importe(cantidad, precio)
print(resultado)  # 24
```

Los nombres del programa principal no tienen que coincidir con los de los parámetros. Por posición, el primer argumento llega al primer parámetro.

También puedes nombrar argumentos:

```python
def calcular_importe(unidades, precio_unitario):
    return unidades * precio_unitario

print(calcular_importe(precio_unitario=6, unidades=4))  # 24
```

## 3. return y print: dos tareas diferentes

- print muestra información en la consola.
- return entrega un valor al código que llamó a la función y termina esa llamada.

```python
def mostrar_doble(numero):
    print(numero * 2)

resultado = mostrar_doble(5)  # Muestra 10
print(resultado)            # Muestra None
```

Como no hay return con un valor, la función devuelve None. La pantalla mostró 10, pero ese 10 no se entregó como resultado.

```python
def obtener_doble(numero):
    return numero * 2

resultado = obtener_doble(5)
print(resultado + 3)  # 13
```

Aquí puedes reutilizar el resultado en otra operación. La función no imprime nada por sí misma.

En tus proyectos, las funciones de cálculo y comprobación suelen devolver resultados; main.py solicita entradas y los muestra. Algunas funciones de formato o notificación deben imprimir porque lo pide el enunciado: revisa el contrato concreto.

## 4. Valores por defecto

```python
def aplicar_descuento(precio, porcentaje=10):
    return precio * (1 - porcentaje / 100)

print(aplicar_descuento(80))      # 72.0
print(aplicar_descuento(80, 25))  # 60.0
```

El valor por defecto se utiliza **solo si omites ese argumento**. Si lo pasas, sustituyes el predeterminado.

Esto explica el proyecto 26: pasar el mes actual a una función que lo compara con el mes actual hace que coincidan. Para comprobar noviembre, omites el argumento si su valor por defecto es 11, o pasas 11.

En estas definiciones sencillas, los parámetros obligatorios van antes que los que tienen valor por defecto.

## 5. Funciones sin parámetros y resultados booleanos

Una función puede obtener sus datos del sistema, sin recibir argumentos: por ejemplo, consultar la hora actual.

Otra puede devolver un bool:

```python
def supera_limite(cantidad, limite=100):
    return cantidad > limite

if supera_limite(120):
    print("Límite superado")
```

No necesitas escribir un if dentro de la función para devolver True o False: la comparación ya produce ese valor.

## 6. Variables locales y flujo de valores

Los parámetros y variables creados dentro de una función son locales a esa llamada.

```python
def sumar_tasa(base):
    tasa = base * 0.1
    return base + tasa

total = sumar_tasa(50)
print(total)  # 55.0
```

Fuera no puedes utilizar tasa como si estuviera definida allí. Devuelve lo que necesites en lugar de depender de variables globales.

Después de return no se ejecutan más instrucciones de esa llamada. Si hay varias ramas, revisa que todas devuelvan lo esperado; una ruta sin return acaba devolviendo None.

## 7. Leer el contrato antes de implementar

Para cada función de la guía, apunta:

| Pregunta | Ejemplo |
|---|---|
| ¿Qué recibe? | minutos: entero |
| ¿Qué hace? | Multiplica por la tarifa |
| ¿Qué devuelve? | Precio: decimal |
| ¿Qué presupone? | Minutos no negativos |
| ¿Debe imprimir? | No, salvo que se indique |

Un nombre como calcular_precio no convierte automáticamente las entradas ni comprueba su validez. Eso lo determina su implementación.

## Práctica de comprobación

Antes de conectar la consola, prueba llamadas con datos fijos. Comprueba el resultado normal, el límite y los casos especiales que admita el enunciado.

**Errores frecuentes:** olvidar paréntesis al llamar; pasar argumentos en orden incorrecto; imprimir en lugar de devolver; no guardar el resultado; utilizar una variable local desde fuera.

Referencia: [Definición de funciones](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions).
