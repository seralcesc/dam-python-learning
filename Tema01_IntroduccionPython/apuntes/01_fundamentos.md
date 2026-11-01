# 01 · Fundamentos, variables y entrada/salida

[Índice del tema](../README.md) · [Siguiente: cadenas](02_cadenas.md)

**Ejercicios relacionados:** 01–05. Registro de alumno, temperaturas, salario, desglose de tiempo y factura.

## 1. Antes de escribir código: entrada, proceso y salida

Separa el enunciado en tres preguntas:

| Paso | Pregunta | Ejemplo: coste de una compra |
|---|---|---|
| Entrada | ¿Qué datos necesito? | Unidades y precio por unidad |
| Proceso | ¿Qué hago con esos datos? | Multiplicar unidades por precio |
| Salida | ¿Qué debo mostrar? | Importe con dos decimales |

Escribe primero un caso a mano: 3 unidades a 2,50 € deben costar 7,50 €. Después comprueba que el programa produce ese resultado.

## 2. Variables y tipos básicos

Una variable es un nombre al que asignas un valor. En Python no escribes el tipo delante del nombre como en Java.

```python
nombre = "Lucía"       # str: texto
unidades = 3           # int: entero
precio = 2.5          # float: número con parte decimal
disponible = True     # bool: verdadero o falso
```

Usa nombres descriptivos con palabras separadas por guiones bajos: `precio_base`, `total_segundos`. Python distingue mayúsculas: `precio` y `Precio` son nombres distintos.

`=` asigna un valor. No es una comparación.

```python
unidades = 3
unidades = unidades + 2
print(unidades)  # 5
```

La parte derecha se calcula con el valor anterior y el resultado se guarda en la variable.

## 3. input(): lo que escribes llega como texto

```python
nombre = input("Nombre: ")
unidades = int(input("Unidades: "))
precio = float(input("Precio por unidad: "))
```

Aunque escribas 3, `input()` devuelve `"3"`. La conversión depende del uso del dato:

| Expresión | Resultado |
|---|---|
| `int("12")` | Entero 12 |
| `float("12.5")` | Decimal 12.5 |
| `str(12)` | Texto "12" |
| `int(12.9)` | Entero 12; no redondea |

Introduce los decimales con punto: `12.5`. `float("12,5")` e `int("12.5")` provocan `ValueError`. Los primeros ejemplos presuponen entradas numéricas válidas; validar el rango y gestionar texto no numérico son problemas distintos.

Los teléfonos, códigos postales o tarjetas se suelen tratar como texto: no necesitas operar con ellos y pueden tener ceros iniciales.

## 4. Operaciones

| Operador | Uso | Ejemplo y resultado |
|---|---|---|
| `+` | Suma | `7 + 2` → 9 |
| `-` | Resta | `7 - 2` → 5 |
| `*` | Multiplicación | `7 * 2` → 14 |
| `/` | División | `7 / 2` → 3.5 |
| `//` | División redondeada hacia abajo | `7 // 2` → 3 |
| `%` | Resto | `7 % 2` → 1 |
| `**` | Potencia | `3 ** 2` → 9 |

En cantidades enteras no negativas, `//` permite contar grupos completos y `%` obtener lo que sobra. Con negativos, recuerda que redondea hacia abajo: `-7 // 2` es -4.

```python
total_unidades = 53
capacidad = 12

cajas_completas = total_unidades // capacidad  # 4
unidades_sueltas = total_unidades % capacidad  # 5
```

Esta idea se aplica al desglose de tiempo: calcula una unidad grande y continúa con el resto, sin volver a utilizar toda la cantidad original.

Usa paréntesis para expresar el orden de una fórmula. En Python `^` no calcula potencias.

## 5. Mostrar resultados con f-strings

La `f` delante de las comillas permite insertar expresiones entre llaves.

```python
unidades = 3
precio = 2.5
total = unidades * precio

print(f"Has comprado {unidades} unidades.")
print(f"Importe: {total:.2f} €")  # Importe: 7.50 €
```

| Formato | Significado | Ejemplo |
|---|---|---|
| `{valor}` | Mostrar el valor | `f"{3}"` → "3" |
| `{valor:.2f}` | Mostrar dos decimales | `f"{2.5:.2f}"` → "2.50" |
| `{valor:02d}` | Entero de al menos dos posiciones, con ceros | `f"{3:02d}"` → "03" |

`:.2f` cambia la presentación; la variable sigue conservando su valor numérico original. `round(valor, 2)` devuelve un número redondeado, pero no garantiza mostrar dos cifras decimales. Los `float` son aproximaciones binarias; para estas prácticas sirven, aunque algunos cálculos puedan tener pequeñas diferencias de precisión.

Si vienes de Java: las f-strings cubren muchos usos de `String.format` y `printf`, con una sintaxis diferente.

## 6. Porcentajes

El 21 % de una cantidad es `cantidad * 21 / 100`. Distingue el importe del porcentaje y el total:

```python
base = 80
porcentaje = 10
recargo = base * porcentaje / 100
total = base + recargo

print(f"Recargo: {recargo:.2f} €")  # 8.00 €
print(f"Total: {total:.2f} €")      # 88.00 €
```

Para una rebaja, resta el descuento a la base. No confundas el descuento con el precio final.

## 7. Guía de los ejercicios, en orden

| Ejercicio | Cómo plantearlo | Qué comprobar |
|---|---|---|
| 01 · Registro | Leer los tres textos y construir un mensaje con f-string. | Espacios entre nombre y apellidos. |
| 02 · Temperatura | Leer un float, aplicar la conversión y mostrarla. | 0 °C debe dar 32 °F. |
| 03 · Salario | Leer horas y tarifa y multiplicarlas. | La tarifa admite decimales. |
| 04 · Tiempo | Obtener horas completas, trabajar con el resto y obtener minutos y segundos. | Probar 0, 59, 60 y 3600 segundos. |
| 05 · Factura | Separar precio base, importe del IVA y precio final. | Mostrar dos decimales sin convertir antes los números a texto. |

## 8. Errores frecuentes

- `"3" + "2"` produce `"32"`: estás uniendo textos.
- Usar una variable antes de asignarle valor provoca `NameError`.
- Olvidar la `f` imprime las llaves y los nombres literalmente.
- No escribas `int(input)`: necesitas llamar a `input()`.
- No llames a tus variables `str`, `int`, `float` o `input`: ocultarías esos nombres incorporados.

## Consulta rápida

**Leer texto:** `input(...)` · **Leer entero:** `int(input(...))` · **Leer decimal:** `float(input(...))` · **Mostrar:** `print(...)` · **Dos decimales:** `f"{valor:.2f}"`.

Referencia: [Introducción oficial a Python](https://docs.python.org/es/3/tutorial/introduction.html).
